mapboxgl.accessToken = 'pk.eyJ1Ijoiem9lbWFyc2NobmVyIiwiYSI6ImNrYW16eXdibTB1eDgyenBrZXJkb2txZzUifQ.Xbmkj-0Dqf-e1zn_RWuh-Q';
var map = new mapboxgl.Map({
	container: 'map',
	style: 'mapbox://styles/mapbox/streets-v11'
});

function addimage(filename, coord1, coord2, name, sourcename) {
	map.loadImage(filename, function(error, image) {
		if (error) throw error;
		map.addImage(name, image);
		map.addSource(sourcename, {
			'type': 'geojson',
			'data': 
			{
				'type': 'FeatureCollection',
				'features': [
					{
						'type': 'Feature',
						'geometry': 
						{
							'type': 'Point',
							'coordinates': [coord1, coord2]
						}
					}
				]
			}
		});
	});
	map.addLayer(
	{
		'id': 'points',
		'type': 'symbol',
		'source': sourcename,
		'layout': 
		{
			'icon-image': name,
			'icon-size': 0.1
		}
	});

}
 
map.on('load', function() {
 addimage('../images/patscat.jpg', 0, 0, 'cat', 'point1');
 addimage('../images/patscat.jpg', 12.550343, 55.665957, 'copenhagencat', 'point2');
});