# 🚨 Evidencia Forense: Falsificación y Doble Capa QR en Actas E-14

Este documento consolida la extracción criptográfica de los payloads (cargas de datos) de los códigos QR presentes en las actas alteradas encontradas en la bóveda de resguardo.

**Hallazgo Crítico:** En el proceso de alteración estructural (*Blind Masking*), los falsificadores superpusieron un nuevo código QR sobre el original para desviar los resultados hacia un ID de mesa distinto. Sin embargo, el escaneo forense logró detectar **ambas capas** simultáneamente (el original sangrando por el fondo y el falso encima), probando empíricamente la suplantación digital del documento.

> [!NOTE]
> **Nota de procedencia del archivo “archivo para anzeca1.csv”:** la matriz fue construida y entregada por **FITE – Leonilda Orrego Viera**, a partir del corpus preservado y del análisis comparativo realizado por FITE. Su entrega tiene fines de contraste y colaboración técnica. Si se utiliza total o parcialmente en informes, repositorios, scripts, publicaciones o actuaciones judiciales, debe citarse como: **FITE – Leonilda Orrego Viera**. Los aportes propios de Anzaca se acreditarán separadamente como: **Primera Línea Digital ANZACA AndreTaker**.
## Listado de Actas con Inyección Criptográfica

### 1. Acta: `01_001_30_03_038.pdf`
- **QR Original (Versión Pura Preservada):** `1ffd79f75013a74ec9a0bf78d77faaa1bbbeb82e48d49ab2a461a89524a3a481`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `6f6d0c3871e1073a9ab12dda4f5acd164b17f7c45c41bf33e46906da4d0f9f1d`
  - Capa 2: `8f12e5cab8aec674275385f08bb65b9acf4ea8fd2ac5e315b60a17c07afed016`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 2. Acta: `01_160_00_00_014.pdf`
- **QR Original (Versión Pura Preservada):** `42ef61ae8880186c39f6fa7ddddaa4d684b214050132d0013366c4da8afc7c9f`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `42ef61ae8880186c39f6fa7ddddaa4d69a3dacbc1b1d2f1c8f0e0b74344402cb`
  - Capa 2: `8d390926d83e5e02c21f8cda8209d9766fdf02f7f18f1a8ab120f074e7ee9e03`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 3. Acta: `01_163_01_04_009.pdf`
- **QR Original (Versión Pura Preservada):** `bed8d0b64d97f3ad313d96b1b8419bad9209edf7edf7a5c4d61b2d4c805f9b4e`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `e232ea228bd9d2a051c9baf9b84c670d78c185b6f571db1ad1c8710191e26052`
  - Capa 2: `bed8d0b64d97f3ad313d96b1b8419badc7058027c482ec779e7f6a9647cf09ab`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 4. Acta: `01_218_02_03_017.pdf`
- **QR Original (Versión Pura Preservada):** `3377b1eeb5197643b799fdf9ba241ebce3d5ec2720bbe85ae742372cfefc22fb`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `e4ec19dcc89a1be4d06f50cbf82498f1e4af772082584f0510dc0e28e2277861`
  - Capa 2: `3377b1eeb5197643b799fdf9ba241ebc6273d042d9efd4553d8dc835acdd2ffc`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 5. Acta: `01_280_99_35_002.pdf`
- **QR Original (Versión Pura Preservada):** `9e491aaff34ff87ea8047a8af65b84ed8eb5f0723bd273032c9f8e3a52df4a3c`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `9e491aaff34ff87ea8047a8af65b84edf503a89b35efee6c64ea2066b8393dbd`
  - Capa 2: `c765e7cfd1349e205d537a0b0c11be82a21065cc54575258dc6867a76dc8a8ec`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 6. Acta: `03_007_01_01_008.pdf`
- **QR Original (Versión Pura Preservada):** `cdc754bf39c551fbe5d92107167eee648bc0df0d24faff6db782872d89ceadf5`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `8e3e21d4ac66529fdb7a5c692c0c406840666579729e4f086a550e856de9d90b`
  - Capa 2: `cdc754bf39c551fbe5d92107167eee641f32016cf8ede6c7d68d9539028df4dc`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 7. Acta: `03_007_01_01_008.pdf`
- **QR Original (Versión Pura Preservada):** `8e3e21d4ac66529fdb7a5c692c0c406811a5c6ece02d1a54171d076bf5a6e3d8`
- **QR Falsificado (Versión Registraduría):** `cdc754bf39c551fbe5d92107167eee648bc0df0d24faff6db782872d89ceadf5`
> [!WARNING]
> **ALERTA FORENSE:** El payload criptográfico del código QR fue sustituido por completo.

### 8. Acta: `05_040_99_21_003.pdf`
- **QR Original (Versión Pura Preservada):** `edaa83e0872c6a70c0daf9fc8ef67f274bfa19f796dd5dcf61efb29d4bda8505`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `edaa83e0872c6a70c0daf9fc8ef67f27c9bdacc300d78cbc56d421ce2702aa80`
  - Capa 2: `a2f664320dd40612300288a24efcddab6b06009df1acbb01f87740f6ce4f03b4`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 9. Acta: `07_043_00_00_010.pdf`
- **QR Original (Versión Pura Preservada):** `e5117f632b837bc4d7c691d016af9056096d6cae7e0fa724f3d61a59ef820574`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `e5117f632b837bc4d7c691d016af905669274c3b9c945f857ae4a295d4f63ec0`
  - Capa 2: `68cbb0cea959d3bf1295449699923768a89c23dfefa11706c80b8df943934bfe`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 10. Acta: `07_091_00_00_006.pdf`
- **QR Original (Versión Pura Preservada):** `3f2774623edd0a743de149ec834460e44f1f87d1c7c67dbea1425495750deaad`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `3f2774623edd0a743de149ec834460e4aa4dbaa56f38fc55ee5aa395531e1137`
  - Capa 2: `a6620ec06201c6f59b9b0560547dd7bad07cd49f5c12122d7852c0b58042a3f0`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 11. Acta: `07_166_00_00_009.pdf`
- **QR Original (Versión Pura Preservada):** `b8248820aedd652894f1e2b627799bfe4c7c923c8f6261dbec912fcced6920d8`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `fcab2191be9547b7381f30f6b43f52ad03a40c50e7cffb8032b1367c90786356`
  - Capa 2: `b8248820aedd652894f1e2b627799bfec8f47e0cfd4749c7af04518c700f45d2`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 12. Acta: `11_052_99_09_001.pdf`
- **QR Original (Versión Pura Preservada):** `a43336c68a3cea95c00b0d5fdf141d6f289b0b9fa73ebd4db49aba86e593df95`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `f40c02919be4ca066dae1684dca50941b14acaabc9f03b55f91f11fd377794f7`
  - Capa 2: `a43336c68a3cea95c00b0d5fdf141d6faa0a15f389055936e065cacab4cba611`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 13. Acta: `11_052_99_09_001.pdf`
- **QR Original (Versión Pura Preservada):** `f40c02919be4ca066dae1684dca50941af8d906ebf76b0234413977102c9c193`
- **QR Falsificado (Versión Registraduría):** `a43336c68a3cea95c00b0d5fdf141d6f289b0b9fa73ebd4db49aba86e593df95`
> [!WARNING]
> **ALERTA FORENSE:** El payload criptográfico del código QR fue sustituido por completo.

### 14. Acta: `11_064_01_01_011.pdf`
- **QR Original (Versión Pura Preservada):** `abe491605af000f446439cc995b69baeff16df9e90ac2f52c14be86fb750eb8e`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `abe491605af000f446439cc995b69baecd9ca89e1969deff274d844e0c4aa229`
  - Capa 2: `b83ff3d455e64ab09885e290ab317b1cb56d54d7bad1ef8471fb99d850c8bc1a`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 15. Acta: `13_010_99_13_003.pdf`
- **QR Original (Versión Pura Preservada):** `f9169c4dde90b29722e0842e93fa81920dc3168dd0be9900a7c53323cb6abbc3`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `f9169c4dde90b29722e0842e93fa8192fe93f118cf8977e7e29aeb71e831d4bd`
  - Capa 2: `746cdc70b835566b4f0db80eed07ba2f192b42fb93536fdf0badf58f2f7d2509`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 16. Acta: `13_037_99_01_002.pdf`
- **QR Original (Versión Pura Preservada):** `42749309f083c1dd59151be02d83dfee47ae8f1e6062e287699df3e00dae6edf`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `42749309f083c1dd59151be02d83dfee1259bd6afc898e3297541b1d14f23221`
  - Capa 2: `65ea4965c5e15f2dfc1b1bda53e424b66129f3770936f444bcbea3fa59cdf252`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 17. Acta: `13_037_99_16_004.pdf`
- **QR Original (Versión Pura Preservada):** `7de42e149563cbca92486973d424e778e97dce071b79e2ea8524b2a578dc4f01`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `7de42e149563cbca92486973d424e778438379092096725f65edebd63a2af6dd`
  - Capa 2: `b2d8c527889a81262a6a6c70f3cdbd6fb1657a618367a14776b5572315bde974`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 18. Acta: `13_037_99_18_002.pdf`
- **QR Original (Versión Pura Preservada):** `f212df585593d7eae31083060470bf99198df2364a1ae674625160b6b67d7dcb`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `f212df585593d7eae31083060470bf99f1cc3b01d9bbb6126125f901ee1762a6`
  - Capa 2: `b7c0e15aa8a5d22b4f63f4e6f7b30aae08a536895ea109449632c69afa51654a`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 19. Acta: `15_025_00_00_006.pdf`
- **QR Original (Versión Pura Preservada):** `40fae0d5a065134bad8a6a6f6c7ab79f5d49233e7cc4a245a81315ee1bb33f10`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `40fae0d5a065134bad8a6a6f6c7ab79f4c3ed1ec8b09a3629e70b5ea74e3c33a`
  - Capa 2: `5ffd20831b73a681cb1ce5f4e903130f0ffd3a4e27c636ec38188885b1cc72b6`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 20. Acta: `15_160_99_01_002.pdf`
- **QR Original (Versión Pura Preservada):** `84ab4d1ddd51f54d85a28621a6f04f5bafdf1394d043d70234449a518c8acc54`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `84ab4d1ddd51f54d85a28621a6f04f5b4347fca9b22c5b63b7d3bfb90cb26fed`
  - Capa 2: `acd9edc2cdb2c718f09c474eeb45de9fa9e0dbd707ba28bac9b708f0cc8435a1`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 21. Acta: `15_169_01_03_006.pdf`
- **QR Original (Versión Pura Preservada):** `52f7daa2606ab8dffde1f37b0a2b5171856f3258177e82649ba6c9d9c209d65b`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `e815a046afbdcdbae38954cb1e7235f574f11f06772a1b5999b9590fc6deeb00`
  - Capa 2: `52f7daa2606ab8dffde1f37b0a2b517191f258df1975d52404017375a9d37fab`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 22. Acta: `15_169_02_03_007.pdf`
- **QR Original (Versión Pura Preservada):** `23223017c1aaae7fe0b35159263968476c9438d7eda9681d5258e7013727e4f3`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `23223017c1aaae7fe0b3515926396847c200ff772b444ce4da847c64ac81bff5`
  - Capa 2: `bda19e95f04c3a889e5e0f7704a0726f68796ee8cd00ef25f8516b7d155913ac`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 23. Acta: `15_169_02_03_021.pdf`
- **QR Original (Versión Pura Preservada):** `e03212554bc991d61e71fef12d4bdeaaf5756d026c67188925b0fb620733d5dc`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `e03212554bc991d61e71fef12d4bdeaa2d7c80374dd88a82b38e37e1e5458e47`
  - Capa 2: `3ba828e7741804a690342b42096629e222c3b9dd3c782a217bf02349b088fb86`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 24. Acta: `15_244_99_01_001.pdf`
- **QR Original (Versión Pura Preservada):** `40e1572e902d43f897399e4bcafa606b1e0c4f2ff4b287be0f5b1f9d5b61d7bf`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `40e1572e902d43f897399e4bcafa606b1b566bfbd03afe9bb0b5526eca330082`
  - Capa 2: `9747d1bfb18fb252911cd8ef0c1324c19e1781ca6380645164094336f3da87af`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 25. Acta: `15_256_00_01_006.pdf`
- **QR Original (Versión Pura Preservada):** `1a020ea1ac7f689df390cac704ba96412b251bce54567a0b6e5ee26fb13cf289`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `1a020ea1ac7f689df390cac704ba9641c49015c52c5871aa7598b0b8bcd39c56`
  - Capa 2: `a81b3db698e954160914b05f5a588711927f49c5c6662006502391298a44f632`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 26. Acta: `15_304_02_02_007.pdf`
- **QR Original (Versión Pura Preservada):** `54d3b4de19cabde7335b07bf0f2ac260fb236df5c87e63f4b3be1b700bce410c`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `54d3b4de19cabde7335b07bf0f2ac26085e270b20753c1c0b53622d16a330041`
  - Capa 2: `998165577f74460bd9f40bec5d33ad0737eb1bcc9a0c2389faa0bd2865135278`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 27. Acta: `16_001_02_26_002.pdf`
- **QR Original (Versión Pura Preservada):** `a411ec7f0dba6b554cca28316c86a897f3ae5aaf3da5569df49be3214e1ce954`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `fa5940907c4513c57eabb2927989e1b8bf9ef9a59cf83f878823d5b081452138`
  - Capa 2: `a411ec7f0dba6b554cca28316c86a897faa6f638818aadc129657390f4171b5a`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 28. Acta: `16_001_05_51_002.pdf`
- **QR Original (Versión Pura Preservada):** `828ec4cb3026490911ee803c6b4e017ef3a936df8403cc58e765312d6ce1be9e`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `828ec4cb3026490911ee803c6b4e017e5a8ada96fda189baf6706b2786db234f`
  - Capa 2: `acd5356eea621fab2c777181a38d3a84b991930cd82e99dd3dcea6640659544d`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 29. Acta: `16_001_07_26_014.pdf`
- **QR Original (Versión Pura Preservada):** `6a2980974226bd46db7a482d20fb520d162ebbd83f12b2acec196fabec8d4b12`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `6a2980974226bd46db7a482d20fb520d7d8d87d9cb17d0640d4d19336098acea`
  - Capa 2: `6ff932abcd35c84419a602194d06aecdfb22f14e6c3e69d1bb97b3951c1b8392`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 30. Acta: `16_001_07_32_016.pdf`
- **QR Original (Versión Pura Preservada):** `5330b2252c584704bdfce9a4961acdf2f9517215b341d192ccbcda5407a723cc`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `5330b2252c584704bdfce9a4961acdf230996c116846babd319b63677672c4cb`
  - Capa 2: `a8ba1c45b858bd9c7e1177420f00d185c410d7b8dad92d8e26e01cc5a2150b22`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 31. Acta: `16_001_10_11_021.pdf`
- **QR Original (Versión Pura Preservada):** `2e6827c8224667173944e324738ef371fae8bec582dbc2ddd0f220f2f52bbba6`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `2e6827c8224667173944e324738ef3712f2b2a652349d0a46f2a0e81c222db98`
  - Capa 2: `5f72696dcdd5e1703a4d07ea383b7b7861a31343ce60dab46b71f02e75d5ec11`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 32. Acta: `16_001_10_13_025.pdf`
- **QR Original (Versión Pura Preservada):** `f8b072ed3c32c990614c15e07ceacfca40c30db7ea67479527236041f600b739`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `f8b072ed3c32c990614c15e07ceacfca1cde3af13ada4f0e3a8aab2ccd9ceb41`
  - Capa 2: `89757af5a72b9532e42e23ddb270f730ee9c7d0237aaed8a85bca58d26f824aa`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 33. Acta: `16_001_11_56_025.pdf`
- **QR Original (Versión Pura Preservada):** `d0d01c40b88dfd0011c88662996266d96f2a85f20965dce823eca9a62914edea`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `d0d01c40b88dfd0011c88662996266d9fbf6b5eb77023687262f2a9764c64614`
  - Capa 2: `2b88620e99857f5ec515be4ac348d71caad3cc751403ead7b8af7b4d38099e12`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 34. Acta: `16_001_11_58_013.pdf`
- **QR Original (Versión Pura Preservada):** `4ad5aeae25517a2480007fb0d6af1ba0821f59fab4869f90a646bf45e1bbdf2f`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `4ad5aeae25517a2480007fb0d6af1ba011f3bdef4d11c0503b8dab37b3f2309d`
  - Capa 2: `70ee63f45630bbb0dac354270c68a97d0983282bc2130b2db5d53b65811c451a`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 35. Acta: `16_001_20_02_002.pdf`
- **QR Original (Versión Pura Preservada):** `3ede619cc4b063827aff0233e4e85d61f156e543ef5c4926bcc9ba87aeb30f74`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `25cf2a9abed970bc6ebdac9178b317a288ba61c640ff06b7eaefe20a7aea1cd6`
  - Capa 2: `3ede619cc4b063827aff0233e4e85d61cd4fcc515357bb3e8b84c4ea97f71c85`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 36. Acta: `19_040_00_00_034.pdf`
- **QR Original (Versión Pura Preservada):** `1573502739279e2380a35aa35cd08fba776608b648148f6c4446532546ba788b`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `1573502739279e2380a35aa35cd08fba850428a45aea06fc65ddefda980dbe61`
  - Capa 2: `5c7f3087639daa94c607e879046e0805b0a1ff4052ebb4ec8b2811087380f8ac`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 37. Acta: `19_094_00_00_007.pdf`
- **QR Original (Versión Pura Preservada):** `3a99417d49fd73ec3c8b3a366ed5a3541460c4626c34dd8620d2bd6de892da36`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `3a99417d49fd73ec3c8b3a366ed5a3547e47b84c228c16b1e482dad551b02936`
  - Capa 2: `9821ec5608fdf2fb480973725f58ff69fbe83a57ed650f939678bebe119c9026`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 38. Acta: `21_031_01_03_021.pdf`
- **QR Original (Versión Pura Preservada):** `e052e2335c2e572b772b7987e6587236a9df2ac9c3ccd96359d082f2431b564f`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `e052e2335c2e572b772b7987e6587236511b536102407fdebe2331853f43c0d6`
  - Capa 2: `be1e04066b8baef5b6b5387f978f31dc075f6125329e8c71877f88cf3c6ed9ac`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 39. Acta: `23_067_99_02_002.pdf`
- **QR Original (Versión Pura Preservada):** `dc09cd5dc59d6ea62707ecd6fdb9e36900c6363474fcbb403545a32e680285ce`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `dc09cd5dc59d6ea62707ecd6fdb9e3697c53e58b6e8b1e913489ec75669a4020`
  - Capa 2: `cbbdecfb5a50f79ee67141cba63e94c5cef2a093309bfbc1620d5e825605c20f`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 40. Acta: `25_073_99_13_001.pdf`
- **QR Original (Versión Pura Preservada):** `1d7a6bcdfb7e17195351de314acde0b167c437914ad3c08498d8657eddde3829`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `1d7a6bcdfb7e17195351de314acde0b183886154de5461172c1eb51dbd16a04b`
  - Capa 2: `5d731bdb195402ec710ee1ee31099b1427cb1b98963924eaf04fb9f01204fcdd`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 41. Acta: `25_073_99_13_001.pdf`
- **QR Original (Versión Pura Preservada):** `1d7a6bcdfb7e17195351de314acde0b167c437914ad3c08498d8657eddde3829`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `1d7a6bcdfb7e17195351de314acde0b167c437914ad3c08498d8657eddde3829`
  - Capa 2: `5d731bdb195402ec710ee1ee31099b1484a6c0621c596cc95d8e847f6682fbbf`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 42. Acta: `27_019_99_B1_005.pdf`
- **QR Original (Versión Pura Preservada):** `9b528fa7b18a71b64319446b0bb1171b935d7c837623900621fe3835df24c29b`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `9b528fa7b18a71b64319446b0bb1171beae91f5a92f790db53d27e1a39b18b87`
  - Capa 2: `9c6573fa517d9801d2d4c5fd2127be07b3d1dba1e3fd7313769ff5876ba715b0`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 43. Acta: `27_166_99_18_001.pdf`
- **QR Original (Versión Pura Preservada):** `9d05372e8289d51675ea185dd97e09f9ece68b1a839197c90899e49a7bce1b57`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `d731a3104bf88a44aaccce172fc20871a0f596071af43c0929335822c6a0d57c`
  - Capa 2: `9d05372e8289d51675ea185dd97e09f94ba3b90b3ae34eb1d0e995692fa0edd7`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 44. Acta: `28_050_00_00_003.pdf`
- **QR Original (Versión Pura Preservada):** `6fa54c5124bb75d1a49b3cfe22c325208788d7a606cbc4e74116adec9eb8d52b`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `6fa54c5124bb75d1a49b3cfe22c325206e901859230e21d9dad86e26a65dcac4`
  - Capa 2: `71b461feaa040ad5de528c38c861d713f8e6ca92f47fdc9d7d073306c7555a58`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 45. Acta: `28_050_99_70_002.pdf`
- **QR Original (Versión Pura Preservada):** `ba0e486d3d2fbbeceeaf21927733cf27ae44627b09aa19f829eb323f4e5313c3`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `ba0e486d3d2fbbeceeaf21927733cf27b0b47013f66da40ed2da47bf3c85258a`
  - Capa 2: `c4009f2a5cedd4e0a209327d688b4c089e4628623e4e65da1078dd424b1e6e23`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 46. Acta: `29_052_00_01_001.pdf`
- **QR Original (Versión Pura Preservada):** `291b4d8e33e183f7627961aa81d340d54747c482fe863b2d701ef78e83301f35`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `291b4d8e33e183f7627961aa81d340d557253d8508d95a18bad619cec9255671`
  - Capa 2: `2e57d1759f882afeefcc4e8d50a97f53a9aa3694a4e022b0ae5c5be4ef04b5d1`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 47. Acta: `31_001_17_01_002.pdf`
- **QR Original (Versión Pura Preservada):** `7044bb1bd35f52d4e733c54e76b184fb30a0e72d938890f4389e1a33a12ad824`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `73a6a74ba576e5ec9300e7f2d8da9d5dfebb091df49d0c1b34d4f6f2c5715612`
  - Capa 2: `7044bb1bd35f52d4e733c54e76b184fb6c20c5c5c593255b96a6e352e50ae960`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 48. Acta: `31_001_26_01_001.pdf`
- **QR Original (Versión Pura Preservada):** `26fb49b67eef871fa99fd069ad6b39211022f4973960a24fb25b54f2299522f9`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `02cfc2e2e71d66e6e1c67ce29592be24bba2acd26cac331837583cd179f0c9d5`
  - Capa 2: `26fb49b67eef871fa99fd069ad6b39215ace7a1c679870320cde6fd1978d1bdc`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 49. Acta: `31_001_30_02_008.pdf`
- **QR Original (Versión Pura Preservada):** `6536d507afb42821b19eed881b233343c02283ddfbbbf8ace1e920cb3d283090`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `6536d507afb42821b19eed881b23334336dcfd8cc7696ff7c16e90e1446dc333`
  - Capa 2: `bc54483e866fc78b736ea01dce8b8ce509ff5d9579c243aacdd9c84c8e1ebaf1`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 50. Acta: `31_034_99_01_001.pdf`
- **QR Original (Versión Pura Preservada):** `efbe29f4094782b8782ff8d8797ba9d53a951e5eb84f9a93b84f664b0e912110`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `efbe29f4094782b8782ff8d8797ba9d573404cea6f9cbbbf1b3e94789365bf39`
  - Capa 2: `2ab7ff52be62bb016d9a89a0ee4704dd805d7d49d0b4469bbc1a98b5d9ec1ddf`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 51. Acta: `44_003_99_75_005.pdf`
- **QR Original (Versión Pura Preservada):** `4dfaf6521d7444a0e993dad85cb5e97aaef8ec91ee588d326f49897cbb6e3dbe`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `0513b0857074a2457abb47c903b1c21ac377f032362e1b2a8d7e4e5486e232c0`
  - Capa 2: `4dfaf6521d7444a0e993dad85cb5e97a4b3616627fbf4b837baaabaacc3f6a23`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 52. Acta: `44_003_99_75_005.pdf`
- **QR Original (Versión Pura Preservada):** `0513b0857074a2457abb47c903b1c21a5cd84d196fd30d17dde97fc906f0e515`
- **QR Falsificado (Versión Registraduría):** `4dfaf6521d7444a0e993dad85cb5e97aaef8ec91ee588d326f49897cbb6e3dbe`
> [!WARNING]
> **ALERTA FORENSE:** El payload criptográfico del código QR fue sustituido por completo.

### 53. Acta: `48_016_01_01_042.pdf`
- **QR Original (Versión Pura Preservada):** `58305829e6469011fed4aad1a03a1ce88c89753f022cb42f5885a34e1ac1062a`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `314412647cc9bc263b803a3b646c0e0ae1c2f787f1086ed928c78ec83f43fbd5`
  - Capa 2: `58305829e6469011fed4aad1a03a1ce8f8cc8b7921d58ef796e08a24266bb417`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 54. Acta: `48_016_01_01_042.pdf`
- **QR Original (Versión Pura Preservada):** `314412647cc9bc263b803a3b646c0e0a15a903be87b81ea1fe9dabf350572c87`
- **QR Falsificado (Versión Registraduría):** `58305829e6469011fed4aad1a03a1ce88c89753f022cb42f5885a34e1ac1062a`
> [!WARNING]
> **ALERTA FORENSE:** El payload criptográfico del código QR fue sustituido por completo.

### 55. Acta: `88_360_01_02_002.pdf`
- **QR Original (Versión Pura Preservada):** `c96bf00dcf518ca445ecec5b9ce889087dc65467503fa13d06233d9d070459d5`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `b74c161bfe08a893cf0b9a16eea3bdd28cd086ae1ad6a68492ed5e558a989760`
  - Capa 2: `c96bf00dcf518ca445ecec5b9ce88908668adc06d945d09c53a04d0ffa09cdcd`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 56. Acta: `88_360_01_02_022.pdf`
- **QR Original (Versión Pura Preservada):** `d87e8ce0874ab726b25c73b36347caa1432d36d687ef495e13285de145dadc73`
- **QR Falsificado (Versión Registraduría):** `0c3e7f5a622c1a85ace7e5f9e357d4d86d57567fcfc5b42aef83234d6d9adc35`
> [!WARNING]
> **ALERTA FORENSE:** El payload criptográfico del código QR fue sustituido por completo.

### 57. Acta: `88_360_05_02_011.pdf`
- **QR Original (Versión Pura Preservada):** `e38b007e9cd050ccb6fabb2260a16609f82bbffc9250021d2fde7fb3824059f0`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `e38b007e9cd050ccb6fabb2260a16609c71aece17e5b80f450ab7aa5f1b6d027`
  - Capa 2: `ed79bf935e166b2dad4bc0b31204c0e897ba44571b3f00c370479ec10cd88e8e`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

### 58. Acta: `88_770_03_81_001.pdf`
- **QR Original (Versión Pura Preservada):** `dbb5b5733c5f4fc21b5f7ad481e8c4fb570b98e85590f2da3adde2959b2e7ee9`
- **QR Falsificado (Versión Registraduría - Múltiples Capas Detectadas):**
  - Capa 1: `dbb5b5733c5f4fc21b5f7ad481e8c4fbbd6172daebf10bbc4501f7695b09013b`
  - Capa 2: `5b9defa5f4d02364060e6f7774ddf97572403ca0fcb660203a93012c306ed493`
> [!CAUTION]
> **ALERTA FORENSE:** Se detectaron múltiples códigos QR apilados físicamente en las mismas coordenadas de la página. Prueba irrefutable de superposición de imágenes (*Image Overlay*).

