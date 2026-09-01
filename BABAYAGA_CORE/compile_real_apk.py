#!/usr/bin/env python3
"""
===============================================================================
BABAYAGA CORE — COMPILADOR REAL DE APLICACIÓN NATIVA ANDROID (.APK)
===============================================================================
Autores: AnZaCa (Andrea Zabala Cárcamo) & AndreTaker Cyberdefense Unit
Descripción: Script de compilación atómica que construye, ensambla, alinea
y firma un binario nativo independiente Android (.apk) para el Motorola edge 50.
===============================================================================
"""

import os
import sys
import subprocess
import shutil

SDK = "/home/andrea-zabala-c/Android/Sdk"
BUILD_TOOLS = os.path.join(SDK, "build-tools/34.0.0")
PLATFORM_JAR = os.path.join(SDK, "platforms/android-34/android.jar")
AAPT = os.path.join(BUILD_TOOLS, "aapt")
D8 = os.path.join(BUILD_TOOLS, "d8")
APKSIGNER = os.path.join(BUILD_TOOLS, "apksigner")
ZIPALIGN = os.path.join(BUILD_TOOLS, "zipalign")

WORK_DIR = "/tmp/apk_build_work"
OUTPUT_APK = "/home/andrea-zabala-c/Downloads/AndreTaker_BaBaYaga_Core_REAL.apk"

def log(msg):
    print(f"📱 [Compilador APK Real] {msg}")

def main():
    log("Iniciando compilación de binario APK nativo independiente...")
    shutil.rmtree(WORK_DIR, ignore_errors=True)
    
    src_dir = os.path.join(WORK_DIR, "src", "com", "babayaga", "andretaker")
    assets_dir = os.path.join(WORK_DIR, "assets")
    res_dir = os.path.join(WORK_DIR, "res", "values")
    obj_dir = os.path.join(WORK_DIR, "obj")
    
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(res_dir, exist_ok=True)
    os.makedirs(obj_dir, exist_ok=True)

    # 1. Manifest
    manifest_content = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.babayaga.andretaker"
    android:versionCode="1"
    android:versionName="2.1">
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <application
        android:label="BaBaYaga Core"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
        android:allowBackup="true">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>"""
    with open(os.path.join(WORK_DIR, "AndroidManifest.xml"), "w") as f:
        f.write(manifest_content)

    # 2. Strings
    with open(os.path.join(res_dir, "strings.xml"), "w") as f:
        f.write('<resources><string name="app_name">BaBaYaga Core</string></resources>')

    # 3. Java Source
    java_code = """package com.babayaga.andretaker;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        webView = new WebView(this);
        setContentView(webView);

        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setAllowFileAccess(true);
        ws.setAllowContentAccess(true);
        ws.setAllowFileAccessFromFileURLs(true);
        ws.setAllowUniversalAccessFromFileURLs(true);

        webView.setWebViewClient(new WebViewClient());
        webView.loadUrl("file:///android_asset/index.html");
    }

    @Override
    public void onBackPressed() {
        if (webView != null && webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}"""
    with open(os.path.join(src_dir, "MainActivity.java"), "w") as f:
        f.write(java_code)

    # 4. Copy Web Assets
    repo_dir = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep"
    shutil.copy(os.path.join(repo_dir, "index.html"), os.path.join(assets_dir, "index.html"))
    shutil.copy(os.path.join(repo_dir, "index.css"), os.path.join(assets_dir, "index.css"))
    
    if os.path.exists(os.path.join(repo_dir, "assets")):
        shutil.copytree(os.path.join(repo_dir, "assets"), os.path.join(assets_dir, "assets"), dirs_exist_ok=True)

    # 5. AAPT Package
    apk_unaligned = os.path.join(WORK_DIR, "app-unaligned.apk")
    aapt_cmd = [
        AAPT, "package", "-f", "-m",
        "-J", os.path.join(WORK_DIR, "src"),
        "-M", os.path.join(WORK_DIR, "AndroidManifest.xml"),
        "-S", os.path.join(WORK_DIR, "res"),
        "-A", assets_dir,
        "-I", PLATFORM_JAR,
        "-F", apk_unaligned
    ]
    log("Ejecutando empaquetado inicial AAPT...")
    subprocess.run(aapt_cmd, check=True)

    # 6. Javac Compile
    r_java = os.path.join(src_dir, "R.java")
    main_java = os.path.join(src_dir, "MainActivity.java")
    javac_cmd = [
        "javac", "-classpath", PLATFORM_JAR,
        "-d", obj_dir, r_java, main_java
    ]
    log("Compilando código fuente Java...")
    subprocess.run(javac_cmd, check=True)

    # 7. D8 Dexing
    d8_cmd = [D8, "--output", WORK_DIR, os.path.join(obj_dir, "com", "babayaga", "andretaker", "MainActivity.class"), os.path.join(obj_dir, "com", "babayaga", "andretaker", "R.class")]
    log("Transformando bytecode a DEX (d8)...")
    subprocess.run(d8_cmd, check=True)

    # 8. Add classes.dex
    log("Inyectando classes.dex en paquete APK...")
    subprocess.run(f"cd {WORK_DIR} && zip -u {apk_unaligned} classes.dex", shell=True, check=True)

    # 9. Zipalign
    apk_aligned = os.path.join(WORK_DIR, "app-aligned.apk")
    log("Alineando optimización de memoria (zipalign)...")
    subprocess.run([ZIPALIGN, "-v", "4", apk_unaligned, apk_aligned], check=True)

    # 10. Generate Keystore & Sign APK
    keystore = os.path.join(WORK_DIR, "debug.keystore")
    log("Generando firma de seguridad digital criptográfica...")
    keytool_cmd = [
        "keytool", "-genkey", "-v",
        "-keystore", keystore,
        "-alias", "androiddebugkey",
        "-storepass", "android",
        "-keypass", "android",
        "-keyalg", "RSA",
        "-keysize", "2048",
        "-validity", "10000",
        "-dname", "CN=Android Debug,O=Android,C=US"
    ]
    subprocess.run(keytool_cmd, check=True)

    log("Firmando binario APK con apksigner...")
    sign_cmd = [
        APKSIGNER, "sign",
        "--ks", keystore,
        "--ks-pass", "pass:android",
        "--key-pass", "pass:android",
        "--out", OUTPUT_APK,
        apk_aligned
    ]
    subprocess.run(sign_cmd, check=True)

    size_mb = round(os.path.getsize(OUTPUT_APK) / (1024 * 1024), 2)
    log(f"🎉 ¡APK NATIVO REAL COMPILADO Y FIRMADO CON ÉXITO!")
    log(f"📍 Ubicación: {OUTPUT_APK}")
    log(f"⚖️ Tamaño: {size_mb} MB")

if __name__ == "__main__":
    main()
