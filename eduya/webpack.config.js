var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')


module.exports = {
  context: __dirname,
  entry: [
      'react-hot-loader/patch',
      'webpack-dev-server/client?http://localhost:8080',
      'webpack/hot/only-dev-server',
      './apps/static/js/index'
  ],

  output: {
      path: path.resolve('./apps/static/bundles/'),
      filename: '[name]-[hash].js',
      publicPath: 'http://localhost:3000/static/bundles/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {
    loaders: [
      // we pass the output from babel loader to react-hot loader
      { test: /\.jsx?$/, exclude: /node_modules/, loaders: ['react-hot-loader/webpack', 'babel-loader'], },
    ],
  },

  resolve: {
    alias: { 'react/lib/ReactMount': 'react-dom/lib/ReactMount' },
    modules: ['node_modules', 'bower_components'],
    extensions: ['.js', '.jsx']
  }
}

