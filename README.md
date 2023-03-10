# 馃搱 Cuadro de mandos personal 馃搳

## Introducci贸n
Dise帽o de un cuadro de mandos personal para visualizaci贸n e interacci贸n con un conjunto de datos.
He escogido realizar mi trabajo sobre los alojamientos Airbnb en Barcelona. El cuadro de mandos permite filtrar por opciones y representa los alojamientos en un mapa.

## B煤squeda y documentaci贸n de los datos
He encontrado un dataset en [Kaggle](https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities?select=barcelona_weekdays.csv) con los datos de los precios de los alojamientos de varias ciudades de Europa y he escogido Barcelona. La fuente de los datos es de [Zenodo](https://zenodo.org/record/4446043#.Y9Y9ENJBwUE).

Los datos est谩n en formato csv y contienen los siguientes campos:
- realSum: el precio total del alojamiento para dos personas y dos noches en EUR
- room_type: el tipo de alojamiento
- room_shared: variable dummy para habitaciones compartidas
- room_private: variable dummy para habitaciones privadas
- person_capacity: el n煤mero m谩ximo de hu茅spedes
- host_is_superhost: variable dummy para el estado de superhost
- multi: variable dummy si el listado pertenece a anfitriones con 2-4 ofertas
- biz: variable dummy si el listado pertenece a anfitriones con m谩s de 4 ofertas
- cleanliness_rating: calificaci贸n de limpieza
- guest_satisfaction_overall: calificaci贸n general del listado
- bedrooms: n煤mero de habitaciones (0 para estudios)
- dist: distancia al centro de la ciudad en km
- metro_dist: distancia a la estaci贸n de metro m谩s cercana en km
- attr_index: 铆ndice de atracci贸n de la ubicaci贸n del listado
- attr_index_norm: 铆ndice de atracci贸n normalizado (0-100)
- rest_index: 铆ndice de restaurantes de la ubicaci贸n del listado
- attr_index_norm: 铆ndice de restaurantes normalizado (0-100)
- lng: longitud de la ubicaci贸n del listado
- lat: latitud de la ubicaci贸n del listado

## Visualizaci贸n de los datos
Para la visualizaci贸n de los datos en Streamlit, he utilizado pandas para representar un pie chart con el rango de precios de la selecci贸n de alojamientos, plotly express para generar dos histogramas con las valoraciones de limpieza y alojamiento y streamlit-folium para representar los alojamientos en un mapa.

## Publicaci贸n de la aplicaci贸n.
Puedes acceder a la aplicaci贸n [aqu铆](https://m-arrojo-streamlit-2---cuadro-de-mandos-personal-m-a-app-3msj37.streamlit.app).
