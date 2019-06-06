var path = require('path');
var outputPath = path.resolve(__dirname, '/src/main/webapp/react');
module.exports = {

    context: path.resolve(__dirname, 'src/main/jsx'),

    entry: {
        main: './MainPage.jsx',
        page1: './Page1Page.jsx'
    },
    devtool: 'sourcemaps',
    cache: true,
    output: {
        path: __dirname,
        filename: './src/main/webapp/react/[name].bundle.js'
    },
    mode: 'none',
    module: {
        rules: [ {
            test: /\.jsx?$/,
            exclude: /(node_modules)/,
            use: {
                loader: 'babel-loader',
                options: {
                    presets: [ '@babel/preset-env', '@babel/preset-react' ]
                }
            }
        }, {
            test: /\.css$/,
            use: [ 'style-loader', 'css-loader' ]
        } ]
    }
    // devServer: {
    //     contentBase: outputPath,
    //     publicPath: '/',
    //     host: '0.0.0.0',
    //     port: 80,
    //     proxy: {
    //         '**': 'http://127.0.0.1:8080'
    //     },
    //     inline: true,
    //     hot: false
    // }

};