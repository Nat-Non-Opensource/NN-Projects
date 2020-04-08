module.exports = {
    "transpileDependencies": [
        "vuetify"
    ],
    devServer: {
        proxy: {
            '/': {
                target: 'http://localhost:39112/',
                'changeOrigin': true,
                'secure': false
            }
        }
    },
    // outputDir: './dist/',
    assetsDir: 'static',
};
