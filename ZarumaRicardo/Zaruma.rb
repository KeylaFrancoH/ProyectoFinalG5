require 'open-uri' # consultar a la plataforma
require 'nokogiri' # formatear, parsear a html
require 'csv' # escribir y leer csv

# nom, id[flag], paises[flag + 1], fortuna[flag + 1], juegos[flag + 1]
class Jugador
  attr_accessor :nombre, :id, :pais, :fortuna, :juego
  def initialize(nombre, id, pais, fortuna, juego)
    @nombre = nombre
    @id = id
    @pais = pais
    @fortuna = fortuna
    @juego = juego
  end

  def guardar
    CSV.open('archivos/informacion.csv', 'a') do |csv|
      csv << [@nombre, @id, @pais, @fortuna, @juego]
    end
  end
end
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
flag = 0
nombres.each do |nom|
  jugador = Jugador.new(nom, id[flag], paises[flag + 1], fortuna[flag + 1], juegos[flag + 1])
  jugador.guardar
  flag += 1
end
