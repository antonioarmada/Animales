# Animales v1.0.1

En el marco de [Programa de Voluntarios](http:/ciencia.chubut.gov.ar/programa-de-voluntarios/) de la *SECRETARÍA DE CIENCIA, TECNOLOGÍA e INNOVACIÓN PRODUCTIVA DE CHUB* dearrollamos un juego simple pensado para ser utilizado con seguidores de pupila de escaza resolución como Gaze Pointer o de alta resolucción como Tobii 4c, en el apoyo terapéutico de aquellos niños y niñas que tengan un compromiso motriz o neurológico, parálisis cerebral, lesión medular, enfermedades neuromusculares, distrofia muscular progresiva o traumatismos de cráneo, ya que les permite interactuar con el movimiento de sus ojos. El uso requiere asistencia del terapeuta.

El juego es muy simple, cuando el/la paciente dirige sus ojos a uno de los animales, el sol se posa arriba y el animal se mueve y emite su sonido característico.

Este software está siendo probado en el Servicio de Rehabilitación Psicomotora del Hospital de Trelew

## Cambios de versión

Primera versión testeandose

## Comenzando 

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo, pruebas y uso final._


### Hardware necesario:

* Opción 1: PC y webcam (utilizar un entorno bien iluminado sin contraluces). Esta configuración es barata y aunque tiene poca resolución (el software está preparado para trabajar así) y la calibración puede ser inestable de una sesión a otra. Utiliza sonido.

* Opción 2: PC y Tobii 4c, esta configuración es má cara pero mejora la precisión y el guardado de los perfiles de calibración.


### Pre-requisitos

* El software fue desarrollado para funcionar en **Windows 10** ya que por el momento es el estandar en los centros de rehabilitación y en las computadoras personales de las familias que lo implementarían. 

* Para el uso con webcam, recomendamos la instalación de [GazePointer](https://sourceforge.net/projects/gazepointer/) y su calibración (puede guardarse para usos futuros en sitiaciones similares)


* En caso de utilizarce un dispositivo Tobii 4C, se deben instalar el driver [Tobii Eye Tracking Core Software](https://gaming.tobii.com/getstarted/) y, aunque se podrían configurar las opciones de accesibilidad de Windows 10 para el control del mouse con este disopositivos, recomendamos no hacerlo e instalar [Tobii Dynavox](https://www.tobiidynavox.com/es/software-apps/recursos-gratuitos/gaze-point-software/) para este propósito por ser más simple la instalación y por tenér un proceso de calibración muy simple y ameno para los niños y niñas.



### Instalación 

1. Descarga o clona este respositorio 
2. Ejectua el archivo .exe dentro de /dist/
3. Ejecuta y calibra GazePointer seleccionando la opción para controlar el puntero.
4. Ejecuta el archivo con extensión _.exe_ que está dentro de la carpeta _dist_


## Deployment

* El software fué desarollado en Python 3 y requiere [PyGame](https://www.pygame.org/wiki/GettingStarted)

## Construido con 

* [Python](https://www.python.org/download/releases/3.0/) - Lenguaje usado
* [PyGame](https://www.pygame.org/wiki/GettingStarted) - Librería para el desarrollo de juegos gráficos en Python

## Contribuyendo 

Por favor lee el [CONTRIBUTING.md](https://github.com/antonioarmada/BlaBla/blob/master/CONTRIBUTING.md) para detalles de nuestro código de conducta.


## Versionado 

Usamos [SemVer](https://semver.org/lang/es/) para el versionado. 

## Autores 

* **Antonio Armada** - _Desarrollo Inicial_ SCTeIP de CHUBUT
* **Viana Rossi** - _Tester_ HOSPITAL DE CHUBUT
* **Yanina Cascon** - _Tester_ HOSPITAL DE CHUBUT

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) que participaron en este proyecto. 

## Licencia 

Este proyecto está bajo la siguiente lincencia GNU General Public License version 3.0 (GPLv3)

## Expresiones de Gratitud 

* Comentá a otros sobre este proyecto 
* Invitale una cerveza a alguien del equipo. 
* Dale las gracias públicamente.
* etc.



---

