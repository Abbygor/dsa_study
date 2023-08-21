<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://arhitac.org/wp-content/uploads/2018/08/occ.png" 
        alt="Logo" 
        width="350" 
        height="204">
  </a>

<h3 align="center">lambda-clevertap-email-hub</h3>
</div>

# Índice de Errores
Lista de errores y posibles causas de estós.

### Error 400
**Nombre:** Bad Request
**Descripción:** El servidor no puede o no procesará la solicitud debido a algo que se percibe como un error del cliente.
**Códigos de Error:**
| Código      | Descripción | Causa |
| ----------- | ----------- | ----------- |
|REQUEST.CLEVERTAP.EVENT.NOT.STRUCT|request body json not contains struct valid|El evento que se esta enviando a la lambda no tiene una estructura JSON valida|
|REQUEST.CLEVERTAP.EVENT.NOT.VALID.NAME|event name is not valid|El nombre del evento no es valido, es decir, no existe su lógica en la lambda|
|REQUEST.CLEVERTAP.EVENT.NOT.VALID.DATA.**DATO**|event data **DATO** is required|Dentro del JSON del evento faltó enviar el parametro **DATO**|

### Error 401
**Nombre:** Unauthorized
**Descripción:** El servidor no puede procesar la solicitud debido a que las credenciales enviadas no son validas.
**Códigos de Error:**
| Código      | Descripción | Causa |
| ----------- | ----------- | ----------- |
|HEADER.X-API-KEY.IS.EMPTY|header request X-API-KEY is empty|El token proporcionado en el header esta vacio|
|HEADER.X-API-KEY.IS.INVALID|header request X-API-KEY is not valid|El token proporcionado en el header es incorrecto|

### Error 404
**Nombre:** Not Found
**Descripción:** El servidor no encuentra el recurso solicitado.
**Códigos de Error:**
| Código      | Descripción | Causa |
| ----------- | ----------- | ----------- |
|BUILD.ResumeID.NOT.FOUND|ResumeID **ID** not found|Indica que no se encontro el **ID** en la tabla de Resumes|
|BUILD.JobID.NOT.FOUND|JobID **ID** not found|Indica que no se encontro el **ID** en el endpoint de jobs|

### Error 500
**Nombre:** Internal Server Error
**Descripción:** Se ha producido un error al intentar acceder al servidor, pero no se puede dar más detalles sobre lo que ha ocurrido.
**Códigos de Error:**
| Código      | Descripción | Causa |
| ----------- | ----------- | ----------- |
|POST.APPLY.INSTANT.GORM.ERROR|N/A|Ocurrio un error al realizar la conexión y/o consulta a la base de datos de OCC|
|Any|N/A|Cualquier otro problema ageno a la lambda|

### Error 503
**Nombre:** Service Unavailable
**Descripción:** El servidor no puede alcanzar el recurso solicitado.
**Códigos de Error:**
| Código      | Descripción | Causa |
| ----------- | ----------- | ----------- |
|POST.APPLY.INSTANT.HTTP.JOBS.CLIENT.ERROR|N/A|Ocurrio un problema al comunicarse con el endpoint de jobs|
|POST.APPLY.INSTANT.HTTP.CLEVERTAP.CLIENT.ERROR|N/A|Ocurrio un problema al comunicarse con el endpoint de clevertap|
