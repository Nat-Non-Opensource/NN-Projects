<template>
	<div style="width: 100%; height: 100%;" class="noScroll">
		<v-app id="app">
			<v-row justify="center">
				<v-dialog v-model="dialog" max-width="21.4%" max-height="23%">
					<v-card>
						<v-card-actions>
							<v-btn color="white darken-2" @click="dialog = false">
								<v-icon dark>mdi-arrow-left</v-icon>Back
							</v-btn>
							<v-spacer></v-spacer>
						</v-card-actions>
						<v-card-title class="headline"> {{ pname }}</v-card-title>
						<v-card-subtitle>
							<p style="display: inline;color: rgb(210, 210, 210);" v-if="pact">
								บริการ
							</p>
							<p style="display: inline;color: rgb(210, 210, 210);" v-else>
								ไม่บริการ
							</p>
						</v-card-subtitle>
						<v-card-text
							><p v-if="ptype === covid19">
								COVID-19: โรงทานน้ำใจ
							</p>
							<p v-else-if="ptype === rescue">
								RESCUE: กู้ภัย
							</p>
							<p v-else-if="ptype === er - hospital">
								ER-HOSPITAL: โรงพยาบาลฉุกเฉิน
							</p>
							<p v-else-if="ptype === 'aed'">
								AED: เครื่องกระตุกหัวใจ
							</p>
							<p v-else>{{ ptype }}: ไม่รู้จัก</p></v-card-text
						>
						<v-card-text> คำอธิบาย: </v-card-text>
						<v-card-text>
							<div class="pre-formatted">{{ pdesc }}</div>
						</v-card-text>
						<v-card-text>
							<a :href="'https://www.google.com/maps/dir//' + plat + ',' + plng"
								>นำทางไปที่ตำแหน่ง</a
							>
						</v-card-text>
						<v-card-text>
							Picture:
						</v-card-text>
					</v-card>
				</v-dialog>
			</v-row>
			<l-map
				:zoom.sync="zoom"
				:options="mapOptions"
				:center="center"
				:bounds="bounds"
				:min-zoom="minZoom"
				:max-zoom="maxZoom"
				style="width: 100%;z-index: 100;"
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
					:attribution="tileProvider.attribution"
					:url="tileProvider.url"
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
				>
					<l-tooltip :content="marker.tooltip" />
					<l-popup :content="marker.tooltip" />
				</l-marker>
				<l-layer-group
					v-for="item in covid191"
					:key="item.id"
					:visible.sync="item.visible"
					layer-type="overlay"
					name="COVID-19: บริการ"
				>
					<l-layer-group :visible="item.markersVisible">
						<l-marker
							v-for="marker in item.markers"
							:key="marker.id"
							:visible="marker.visible"
							:draggable="marker.draggable"
							:lat-lng="marker.position"
							:icon="iconCovid"
							@click="
								dialog = true;
								pname = marker.tooltip;
								pact = marker.active;
								ptype = marker.type;
								pdesc = marker.desc;
								plat = marker.position.lat;
								plng = marker.position.lng;
								pimg = '';
							"
							><l-tooltip :content="marker.tooltip"
						/></l-marker>
					</l-layer-group>
				</l-layer-group>
				<l-layer-group
					v-for="item in covid190"
					:key="item.id"
					:visible.sync="item.visible"
					layer-type="overlay"
					name="COVID-19: ไม่บริการ"
				>
					<l-layer-group :visible="item.markersVisible">
						<l-marker
							v-for="marker in item.markers"
							:key="marker.id"
							:visible="item.visible"
							:draggable="item.draggable"
							:lat-lng="marker.position"
							:icon="iconCovids"
							@click="
								dialog = true;
								pname = marker.tooltip;
								pact = marker.active;
								ptype = marker.type;
								pdesc = marker.desc;
								plat = marker.position.lat;
								plng = marker.position.lng;
								pimg = '';
							"
						/>
					</l-layer-group>
				</l-layer-group>
				<l-layer-group
					v-for="item in rescue1"
					:key="item.id"
					:visible.sync="item.visible"
					layer-type="overlay"
					name="Rescue: กู้ภัย"
				>
					<l-layer-group :visible="item.markersVisible">
						<l-marker
							v-for="marker in item.markers"
							:key="marker.id"
							:visible="marker.visible"
							:draggable="marker.draggable"
							:lat-lng="marker.position"
							@click="
								dialog = true;
								pname = marker.tooltip;
								pact = marker.active;
								ptype = marker.type;
								pdesc = marker.desc;
								plat = marker.position.lat;
								plng = marker.position.lng;
								pimg = '';
							"
						/>
					</l-layer-group>
				</l-layer-group>
				<l-layer-group
					v-for="item in erhospital1"
					:key="item.id"
					:visible.sync="item.visible"
					layer-type="overlay"
					name="ER-Hospital: โรงพยาบาลฉุกเฉิน"
				>
					<l-layer-group :visible="item.markersVisible">
						<l-marker
							v-for="marker in item.markers"
							:key="marker.id"
							:visible="marker.visible"
							:draggable="marker.draggable"
							:lat-lng="marker.position"
							@click="
								dialog = true;
								pname = marker.tooltip;
								pact = marker.active;
								ptype = marker.type;
								pdesc = marker.desc;
								plat = marker.position.lat;
								plng = marker.position.lng;
								pimg = '';
							"
						/>
					</l-layer-group>
				</l-layer-group>
				<l-layer-group
					v-for="item in aed1"
					:key="item.id"
					:visible.sync="item.visible"
					layer-type="overlay"
					name="AED: เครื่องกระตุ้นหัวใจ"
				>
					<l-layer-group :visible="item.markersVisible">
						<l-marker
							v-for="marker in item.markers"
							:key="marker.id"
							:visible="marker.visible"
							:draggable="marker.draggable"
							:lat-lng="marker.position"
							@click="
								dialog = true;
								pname = marker.tooltip;
								pact = marker.active;
								ptype = marker.type;
								pdesc = marker.desc;
								plat = marker.position.lat;
								plng = marker.position.lng;
								pimg = '';
							"
						/>
					</l-layer-group>
				</l-layer-group>
			</l-map>
		</v-app>
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
		LControlZoom,
		LControlAttribution,
		LControlScale,
		LControlLayers
	} from 'vue2-leaflet';
	import axios from 'axios';

	const markersCovid1 = [];
	const markersCovid0 = [];
	const markersRescue = [];
	const markersER = [];
	const markersAED = [];

	const tileProviders = [
		{
			name: 'Open Street Map (Carto)',
			visible: true,
			attribution:
				'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a>',
			url: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
		},
		{
			name: 'Open Street Map (Default)',
			visible: false,
			attribution:
				'&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
			url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
		},
		{
			name: 'Open Street Map (Gray)',
			visible: false,
			attribution:
				'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
			url:
				'https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/{z}/{x}/{y}?access_token=sk.eyJ1IjoicGF3YXQiLCJhIjoiY2s4cjBoMDM5MDUwMzNmcW45ZHd0YWppMyJ9.mEct1P_2b2sLI_5MBrpkRA'
		}
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
			LControlLayers
		},
		mounted() {
			axios.get('/map/').then(response => {
				for (const item of response.data) {
					if (item.place_categories == 'covid19') {
						if (item.place_enable == true) {
							markersCovid1.push({
								position: {
									lat: item.place_latitude,
									lng: item.place_longitude
								},
								tooltip: item.place_name,
								desc: item.place_description,
								types: item.place_categories,
								active: item.place_enable,
								visible: true,
								draggable: false
							});
						} else {
							markersCovid0.push({
								position: {
									lat: item.place_latitude,
									lng: item.place_longitude
								},
								tooltip: item.place_name,
								desc: item.place_description,
								types: item.place_categories,
								active: item.place_enable,
								visible: true,
								draggable: false
							});
						}
					} else if (item.place_categories == 'rescue') {
						markersRescue.push({
							position: {
								lat: item.place_latitude,
								lng: item.place_longitude
							},
							tooltip: item.place_name,
							desc: item.place_description,
							types: item.place_categories,
							active: item.place_enable,
							visible: true,
							draggable: false
						});
					} else if (item.place_categories == 'erhospital') {
						markersER.push({
							position: {
								lat: item.place_latitude,
								lng: item.place_longitude
							},
							tooltip: item.place_name,
							desc: item.place_description,
							types: item.place_categories,
							active: item.place_enable,
							visible: true,
							draggable: false
						});
					} else if (item.place_categories == 'aed') {
						markersAED.push({
							position: {
								lat: item.place_latitude,
								lng: item.place_longitude
							},
							tooltip: item.place_name,
							desc: item.place_description,
							types: item.place_categories,
							active: item.place_enable,
							visible: true,
							draggable: false
						});
					}
				}
			});
		},
		data() {
			return {
				center: [18.7888595, 98.9846145],
				opacity: 0.6,
				tokens:
					'sk.eyJ1IjoicGF3YXQiLCJhIjoiY2s4cjBoMDM5MDUwMzNmcW45ZHd0YWppMyJ9.mEct1P_2b2sLI_5MBrpkRA',
				mapOptions: {
					zoomControl: false,
					attributionControl: false,
					zoomSnap: true
				},
				zoom: 13,
				minZoom: 0.5,
				maxZoom: 19,
				zoomPosition: 'topright',
				attributionPosition: 'bottomright',
				layersPosition: 'topright',
				attributionPrefix: 'Vue2Leaflet',
				Positions: ['topleft', 'topright', 'bottomleft', 'bottomright'],
				imperial: false,
				tileProviders: tileProviders,
				markers: [],
				dialog: false,
				pname: '',
				pact: '',
				ptype: '',
				pdesc: '',
				plat: 0.0,
				plng: 0.0,
				pimg: '',
				covid191: [
					{
						id: 'cv1',
						markers: markersCovid1,
						visible: true,
						markersVisible: true
					}
				],
				covid190: [
					{
						id: 'cv0',
						markers: markersCovid0,
						visible: true,
						markersVisible: true
					}
				],
				rescue1: [
					{
						id: 'rs',
						markers: markersRescue,
						visible: false,
						markersVisible: false
					}
				],
				erhospital1: [
					{
						id: 'er',
						markers: markersER,
						visible: false,
						markersVisible: false
					}
				],
				aed1: [
					{
						id: 'aed',
						markers: markersAED,
						visible: false,
						markersVisible: false
					}
				],
				iconCovid: icon({
					iconUrl: require('./assets/leaf-red.png'),
					shadowUrl: require('./assets/leaf-shadow.png'),
					iconSize: [38, 95],
					shadowSize: [50, 64],
					iconAnchor: [22, 94],
					shadowAnchor: [4, 62],
					popupAnchor: [-3, -76]
				}),
				iconCovids: icon({
					iconUrl: require('./assets/leaf-gray.png'),
					shadowUrl: require('./assets/leaf-shadow.png'),
					iconSize: [38, 95],
					shadowSize: [50, 64],
					iconAnchor: [22, 94],
					shadowAnchor: [4, 62],
					popupAnchor: [-3, -76]
				}),
				bounds: latLngBounds()
			};
		},
		computed: {
			dynamicSize() {
				return [this.iconSize, this.iconSize * 1.15];
			},
			dynamicAnchor() {
				return [this.iconSize / 2, this.iconSize * 1.15];
			}
		}
	};
</script>

<style>
	* {
		font-family: Arial, Helvetica, sans-serif;
	}

	.pre-formatted {
		white-space: pre;
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
