var path = require('path');
var outputPath = path.resolve(__dirname, '/src/main/webapp/react');

module.exports = {

    context: path.resolve(__dirname, 'src/main/jsx'),
    entry : path.join(__dirname,`/src/main/webapp/components/Root.jsx`),

    devtool: 'sourcemaps',
    cache: true,
    output : {
        filename: `bundle.js`,
        path: path.join(__dirname, `/src/main/webapp/public`),
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
    },
    devServer: {
        hot : true,
        contentBase: [
            path.join(__dirname, `/src/main/webapp/public`),
            path.join(__dirname, `/src/main/webapp/components`)],
        watchContentBase: true,
        historyApiFallback: true,
        compress: true,
        port: 9000,
    }

};