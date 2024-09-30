
# AFD Cesar Cipher API

Esta aplicación es una API que utiliza un Autómata Finito Determinista (AFD) para procesar cadenas y aplicar un cifrado César. La API está desarrollada con Flask y tiene un endpoint que permite procesar cadenas de texto, ya sea para cifrar o descifrar usando el AFD.

## Estructura del Proyecto

```
project/
│
├── app.py                # Punto de entrada del servidor Flask
├── afd.py                # Clase AFD y sus funcionalidades
├── cipher.py             # Clase para el cifrado y descifrado César
└── routes.py             # Definición de rutas y controladores
```

### Archivos

- **app.py**: Archivo principal que ejecuta la aplicación Flask.
- **afd.py**: Contiene la definición de la clase AFD, que procesa la cadena en función de las transiciones definidas.
- **cipher.py**: Extiende la clase AFD para implementar los métodos de cifrado y descifrado utilizando el cifrado César.
- **routes.py**: Define las rutas y controladores de la API.

## Uso

1. Inicia la aplicación Flask:

   ```bash
   python app.py
   ```

2. La API estará disponible en `http://127.0.0.1:5000/`.

3. Para procesar una cadena, realiza una solicitud POST al endpoint `/process` con un JSON que contenga el texto que deseas cifrar o descifrar.

### Ejemplo de solicitud

```bash
curl -X POST http://127.0.0.1:5000/process -H "Content-Type: application/json" -d '{"text": "¡Hola, Mundo!"}'
```

### Ejemplo de respuesta

```json
{
  "processed_text": "|Krod, Pxqgr!|"
}
```

## Funcionalidad

### Autómata Finito Determinista (AFD)

- El AFD procesa cadenas de texto y las evalúa en función de su gramática.
- Dependiendo del estado de aceptación del AFD, la cadena será cifrada o descifrada.
## Definición del AFD

- **Q (Conjunto de estados)** -> {q0, q1, q2, q3, q4, q5, q6}
- **Σ (Alfabeto)** -> {(A-Z), (!¡?¿.,λ), |}
- **S (Estado inicial)** -> q0
- **F (Conjunto de estados de aceptación)** -> {q1, q2, q5}

### Tabla de transiciones

| Estados | A-Z  | !¡?¿.,λ  | `PIPELINE`  |
|---------|------|----------|------|
| q0      | q1   | q2       | q3   |
| q1      | q1   | q2       | q2   |
| q2      | q1   | q2       | q2   |
| q3      | q3   | q4       | q5   |
| q4      | q3   | q4       | q5   |
| q5      | q6   | q6       | q3   |
| q6      | q6   | q6       | q6   |
### Cifrado César

- **Cifrado**: Desplaza las letras del alfabeto por un número fijo de posiciones (por defecto 3).
- **Descifrado**: Desplaza las letras en la dirección inversa para recuperar el texto original.

## Endpoints

### POST `/process`

- **Descripción**: Procesa una cadena de texto utilizando el AFD y aplica cifrado César si es necesario.
- **Parámetros**: 
  - `text`: Texto que será procesado.
  
- **Ejemplo de solicitud**:

  ```json
  {
    "text": "¡Hola, Mundo!"
  }
  ```

- **Ejemplo de respuesta**:

  ```json
  {
    "processed_text": "|Krod, Pxqgr!|"
  }
  ```

- **Errores**:
  - Si no se proporciona un texto: 

    ```json
    {
      "error": "No text provided"
    }
    ```

  - Si la cadena es inválida o no puede ser procesada: 

    ```json
    {
      "error": "Texto cifrado incompleto o inválido"
    }
    ```

## Requerimientos

- Python 3.x
- Flask
- Requests (para realizar pruebas)

