# BandKamp API
 
API de registro de bandas e músicos, além de seus albuns e músicas

Deploy da API: https://bandkamp-sprint6-m5.herokuapp.com/api/

Documentação das requisições: https://bandkamp-sprint6-m5.herokuapp.com/api/docs/

## Endpoints do serviço:

POST /musicians/ - Cadastro de músico.

GET /musicians/ - Lista todos os músicos.

GET /musicians/{musician_id}/ - Busca um músico.

PATCH /musicians/{musician_id}/  - Altera completamente ou parcialmente um músico.

DELETE /musicians/{musician_id}/  - Deleta um músico.

POST /musicians/{musician_id}/albums/  - Cria um álbum relacionado com um músico.

GET /musicians/{musician_id}/albums/ - Lista os álbuns de um músico.

POST /musicians/{musician_id}/albums/{album_id}/songs/  - Cria um som relacionado com um álbum.

GET /musicians/{musician_id}/albums/{album_id}/songs/ - Lista os sons de um álbum.
