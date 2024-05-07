Viewer = require('viewerjs')

if _.startsWith window.location.pathname.toLowerCase(), '/docs'
  $ ->
    $body = $('body')
    $body.scrollspy
      target: '.b-docs-sidebar-sub_links'
      offset: 120

    if _.startsWith window.location.pathname.toLowerCase(), '/docs/changelog'
      $('.b-docs-group-images').each ->
        new Viewer this, {
          navbar: true
          title: false
          toolbar: true
          tooltip: false
          transition: false
          movable: false
        }
    else
      $('img').each ->
        new Viewer this, {
          navbar: false
          title: false
          toolbar: false
          tooltip: false
          transition: false
          movable: false
        }

    goToHash = (val) ->
      window.location.hash = val
      $('html, body').animate({
          scrollTop: $('#' + val).offset().top - 80
      }, 0)

    if window.location.hash
      goToHash window.location.hash.slice(1, 777)

    $('.b-docs-sidebar-sub_links a').on 'click', ->
      goToHash $(this).attr('href').slice(1, 777)
      return false

    return
