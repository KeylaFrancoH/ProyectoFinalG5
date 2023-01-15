require 'open-uri' # consultar a la plataforma
require 'nokogiri' # formatear, parsear a html
require 'csv' # escribir y leer csv

link = 'https://www.esportsearnings.com/players'
datosHTML = URI.open(link)
datosParseados = Nokogiri::HTML(datosHTML.read)
# separamos la pagina
listaJuegos = datosParseados.css('.detail_list_box')
cont = 0
id = []
nombres = []
paises = []
fortuna = []
juegos = []
listaJuegos.css('.format_row').each do |post|
  pais = post.css('.detail_list_player').css('img').attr('title')
  paises.append(pais)
  post.css('.detail_list_player').each do |player|
    cont += 1
    id.append(player.inner_text) if cont.odd?
    nombres.append(player.inner_text) if cont.even?
  end
  total = post.css('.border_right').inner_text
  juego = post.css('.border_left').inner_text
  fortuna.append(total)
  juegos.append(juego)
end

CSV.open('archivos/informacion.csv', 'w') do |csv|
    csv << %w"nom id paises fortuna juegos"
  end
flag = 0
nombres.each do |nom|
  puts flag
  puts nom, id[flag], paises[flag + 1], fortuna[flag + 1], juegos[flag + 1]
  puts
  CSV.open('archivos/informacion.csv', 'a') do |csv|
    csv << [nom, id[flag], paises[flag + 1], fortuna[flag + 1], juegos[flag + 1]]
  end
  flag += 1
end
