module.exports = {
	transpileDependencies: ['vuetify'],
	devServer: {
		proxy: {
			'/': {
				target: 'http://127.0.0.1:39112/',
				changeOrigin: true,
				secure: false,
			},
		},
	},
	// outputDir: './dist/',
	assetsDir: 'static',
};
