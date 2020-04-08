<template>
	<!-- Toggle tables -->
	<!-- <table>
			<tr>
				<th>Layer</th>
				<th>Visible</th>
			</tr>
			<tr v-for="(item, index) in stuff" :key="index">
				<td>{{ 'Layer ' + (index + 1) }}</td>
				<td style="text-align: center;">
					<input v-model="item.visible" type="checkbox" />
				</td>
			</tr>
		</table> -->
	<!-- Map -->
	<div style="width: 100%; height: 100%;">
		<l-map
			:zoom.sync="zoom"
			:options="mapOptions"
			:center="center"
			:bounds="bounds"
			:min-zoom="minZoom"
			:max-zoom="maxZoom"
			style="width: 100%;"
		>
			<l-control-layers
				:position="layersPosition"
				:collapsed="false"
				:sort-layers="true"
			/>
			<l-tile-layer
				v-for="tileProvider in tileProviders"
				:key="tileProvider.name"
				:name="tileProvider.name"
				:visible="tileProvider.visible"
				:url="tileProvider.url"
				:attribution="tileProvider.attribution"
				:token="token"
				layer-type="base"
			/>
			<l-control-zoom :position="zoomPosition" />
			<l-control-attribution
				:position="attributionPosition"
				:prefix="attributionPrefix"
			/>
			<l-control-scale :imperial="imperial" />
			<l-marker
				v-for="marker in markers"
				:key="marker.id"
				:visible="marker.visible"
				:draggable="marker.draggable"
				:lat-lng.sync="marker.position"
				:icon="marker.icon"
				@click="alert(marker)"
			>
				<l-popup :content="marker.tooltip" />
				<l-tooltip :content="marker.tooltip" />
			</l-marker>
			<l-layer-group
				v-for="item in stuff1"
				:key="item.id"
				:visible.sync="item.visible"
				layer-type="overlay"
				name="COVID-19"
			>
				<l-layer-group :visible="item.markersVisible">
					<l-marker
						v-for="marker in item.markers"
						:key="marker.id"
						:visible="marker.visible"
						:draggable="marker.draggable"
						:lat-lng="marker.position"
						:icon="iconCovid"
						@click="alert(marker)"
					/>
					<!-- <l-icon
							:icon-size="dynamicSize"
							:icon-anchor="dynamicAnchor"
							icon-url="./assets/leaf-red.png"
							icon-s
						/> -->
					<!-- </l-marker> -->
				</l-layer-group>
			</l-layer-group>

			<l-layer-group
				v-for="item in stuff2"
				:key="item.id"
				:visible.sync="item.visible"
				layer-type="overlay"
				name="Rescue"
			>
				<l-layer-group :visible="item.markersVisible">
					<l-marker
						v-for="marker in item.markers"
						:key="marker.id"
						:visible="marker.visible"
						:draggable="marker.draggable"
						:lat-lng="marker.position"
						@click="alert(marker)"
					/>
				</l-layer-group>
			</l-layer-group>
		</l-map>
	</div>
</template>

<script>
	import { latLngBounds, icon } from 'leaflet';
	import {
		LMap,
		LTileLayer,
		LMarker,
		LLayerGroup,
		LTooltip,
		LPopup,
		// LIcon,
		LControlZoom,
		LControlAttribution,
		LControlScale,
		LControlLayers,
	} from 'vue2-leaflet';
	import axios from 'axios';

	const markers1 = [];
	const markers2 = [];

	const tileProviders = [
		{
			name: 'OpenStreetMap',
			visible: true,
			// attribution:
			// '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
			url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
			// url: 'https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png',
		},
	];

	export default {
		name: 'App',
		components: {
			LMap,
			LTileLayer,
			LMarker,
			LLayerGroup,
			LTooltip,
			LPopup,
			LControlZoom,
			LControlAttribution,
			LControlScale,
			LControlLayers,
		},
		mounted() {
			axios.get('http://127.0.0.1:39112/map/').then((response) => {
				for (const item of response.data) {
					markers1.push({
						position: { lat: item.place_latitude, lng: item.place_longitude },
						tooltip: item.place_name,
						visible: true,
						draggable: false,
					});

					markers2.push({
						position: { lat: item.place_latitude, lng: item.place_longitude },
						tooltip: item.place_name,
						visible: true,
						draggable: false,
					});
				}
			});
		},
		data() {
			return {
				center: [18.7888595, 98.9846145],
				opacity: 0.6,
				token: 'your token if using mapbox',
				mapOptions: {
					zoomControl: false,
					attributionControl: false,
					zoomSnap: true,
				},
				zoom: 13,
				minZoom: 1,
				maxZoom: 21,
				zoomPosition: 'topleft',
				attributionPosition: 'bottomright',
				layersPosition: 'topright',
				attributionPrefix: 'Vue2Leaflet',
				Positions: ['topleft', 'topright', 'bottomleft', 'bottomright'],
				imperial: false,
				tileProviders: tileProviders,
				markers: [
					// {
					// 	id: 'm1',
					// 	position: { lat: 18.7888595, lng: 98.9846145 },
					// 	tooltip: 'Mueang Chiang Mai',
					// 	draggable: true,
					// 	visible: true,
					// },
				],
				stuff1: [
					{
						id: 's1',
						markers: markers1,
						visible: true,
						markersVisible: true,
					},
				],
				stuff2: [
					{
						id: 's2',
						markers: markers2,
						visible: true,
						markersVisible: true,
					},
				],
				iconCovid: icon({
					iconUrl: require('./assets/leaf-red.png'),
					shadowUrl: require('./assets/leaf-shadow.png'),
					iconSize: [38, 95],
					shadowSize: [50, 64],
					iconAnchor: [22, 94],
					shadowAnchor: [4, 62],
					popupAnchor: [-3, -76],
				}),
				bounds: latLngBounds(),
			};
		},

		methods: {
			alert(item) {
				alert('this is ' + JSON.stringify(item));
			},	
			getting() {},
		},
		computed: {
			dynamicSize() {
				return [this.iconSize, this.iconSize * 1.15];
			},
			dynamicAnchor() {
				return [this.iconSize / 2, this.iconSize * 1.15];
			},
		},
	};
</script>

<style>
	* {
		font-family: Arial, Helvetica, sans-serif;
	}

	table {
		font-family: 'Trebuchet MS', Arial, Helvetica, sans-serif;
		border-collapse: collapse;
		width: 100%;
	}

	table td,
	table th {
		border: 1px solid #ddd;
		padding: 8px;
	}

	table tr:nth-child(even) {
		background-color: #f2f2f2;
	}

	table tr:hover {
		background-color: #ddd;
	}

	table th {
		padding-top: 12px;
		padding-bottom: 12px;
		text-align: left;
		background-color: #4caf50;
		color: white;
	}
</style>
