#coding=utf-8
from flask_assets import Bundle

common_css = Bundle(
    'css/bootstrap.min.css',
    'css/font-awesome.min.css',
    'css/ionicons.min.css',
    'css/AdminLTE.css',
    filters='cssmin',
    output='css/common.css'
)

common_js = Bundle(
    'js/bootstrap.min.js',
    'js/AdminLTE/app.js',
    filters='jsmin',
    output='js/common.js'
)
