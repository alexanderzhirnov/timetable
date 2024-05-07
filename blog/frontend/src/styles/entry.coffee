import '@babel/polyfill'

import 'jquery'
import 'bootstrap/dist/css/bootstrap.min.css'
# import 'bootstrap/dist/js/bootstrap.min.js'
import 'bootstrap/js/dist/scrollspy'
import 'viewerjs/dist/viewer.min.css'
import 'viewerjs/dist/viewer.min.js'

import './main'
import './docs/docs'

# Подключаем все остальные файлы
files = require.context('.', true, /(?!entry).*?.(coffee|js|vue)$/)
files.keys().forEach (key) -> files(key)

window.app =
  toggleSidebar: ->
    $('body').toggleClass('mobile-sidebar')