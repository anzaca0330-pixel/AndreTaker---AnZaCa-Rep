import os
import socket

class NetworkAuditor:
    @staticmethod
    def detect_active_vpn() -> dict:
        """
        Detecta si la conexión de red está siendo enrutada a través de interfaces VPN
        comunes (como tunelización OpenVPN, WireGuard, IPSec o ExpressVPN).
        """
        interfaces_vpn = ['tun', 'tap', 'wg', 'ppp', 'utun', 'nord', 'proton', 'express']
        interfaces_detectadas = []
        
        try:
            # Listar las interfaces del sistema de archivos /sys/class/net/
            net_dir = "/sys/class/net"
            if os.path.exists(net_dir):
                for iface in os.listdir(net_dir):
                    if any(vpn in iface.lower() for vpn in interfaces_vpn):
                        interfaces_detectadas.append(iface)
        except Exception as e:
            return {"status": "error", "message": f"Error al leer interfaces: {str(e)}", "vpn_active": False}

        vpn_active = len(interfaces_detectadas) > 0
        return {
            "vpn_active": vpn_active,
            "detected_interfaces": interfaces_detectadas,
            "status": "safe" if vpn_active else "warning (no VPN interface detected)"
        }

    @staticmethod
    def audit_listening_ports() -> list:
        """
        Realiza un escaneo de puertos de escucha locales TCP en la máquina (localhost)
        para alertar si existen puertos abiertos inusuales que puedan indicar troyanos de acceso remoto.
        """
        puertos_escucha = []
        # Lista de puertos de interés común para auditoría
        puertos_comunes = [21, 22, 23, 25, 80, 443, 139, 445, 3389, 5900, 8080, 9050, 9051]
        
        for port in puertos_comunes:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            resultado = s.connect_ex(('127.0.0.1', port))
            if resultado == 0:
                puertos_escucha.append(port)
            s.close()
            
        return puertos_escucha
