mapboxgl.accessToken = 'pk.eyJ1Ijoiem9lbWFyc2NobmVyIiwiYSI6ImNrYW16eXdibTB1eDgyenBrZXJkb2txZzUifQ.Xbmkj-0Dqf-e1zn_RWuh-Q';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11'
});

addimage(error, image, coord1, coord2, name) {
if (error) throw error;
map.addImage(name, image);
map.addSource('point', {
'type': 'geojson',
'data': {
'type': 'FeatureCollection',
'features': [
{
'type': 'Feature',
'geometry': {
'type': 'Point',
'coordinates': [coord1, coord2]
}
}
]
}
}
 
map.on('load', function() {
// for (picture in 'images/') {
// 	map.loadImage(picture,
// 		      function(error,image) {
// 		if (error) throw error;
// 		map.addImage(picture,image);
// 		map.addSource('point', {
// 			'type': 'geojson',
// 			'data': {
// 				'type': 'FeatureCollection',
// 				'features': [
// 					{
// 						'type': 'Feature',
// 						'geometry': {
// 							'type': 'Point',
// 							'coordinates': [0,0]
// 						}
// 					}
// 					]
// 			}
// 		}
// 		map.addLayer({
// 'id': 'points',
// 'type': 'symbol',
// 'source': 'point',
// 'layout': {
// 'icon-image': 'cat',
// 'icon-size': 0.1
// }
// });
// }
// 		      }
// 		      });
map.loadImage(
'images/patscat.jpg', addimage(image, 0, 0, 'cat'));
map.addLayer({
'id': 'points',
'type': 'symbol',
'source': 'point',
'layout': {
'icon-image': 'cat',
'icon-size': 0.1
}
});
}
);
});
