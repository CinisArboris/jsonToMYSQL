import json

objeto = json.load(open("#_file_json", 'r', encoding='UTF-8'))

niveles = [	'pais',
			'departamento',
			'provincia',
			'municipio',
			'localidad',
			'recinto',
			'mesa'
		]

f = open ('insert_freyja.sql','wb')
f.close()


f = open ('insert_freyja.sql','a')

key_municipio = key_localidad = key_recinto = key_provincia = 0

for niveles[0] in objeto:
	c = """insert into `geo_pais` (`id`, `nombre`, `sup`, `geo`) values ("""+str(niveles[0]['pk'])+', "'+str(niveles[0]['nombre'])+'", '+str(777)+', '+str(0)+');'
	f.write(c)
	f.write('\n')
	# ==================================
	for niveles[1] in niveles[0]['departamento']:
		c = """insert into `geo_departamento` (`id`, `nombre`, `sup`, `geo`) values ("""+str(niveles[1]['pk'])+', "'+str(niveles[1]['nombre'])+'"'+', '+str(niveles[0]['pk'])+', '+str(1)+');'
		f.write(c)
		f.write('\n')
		# ==================================
		for niveles[2] in niveles[1]['provincia']:
			#c = """insert into `geo_provincia` (`id`, `nombre`, `sup`, `geo`) values ("""+str(niveles[2]['pk'])+', "'+str(niveles[2]['nombre'])+'"'+', '+str(niveles[1]['pk'])+', '+str(2)+');'
			key_provincia = key_provincia + 1
			c = """insert into `geo_provincia` (`nombre`, `sup`, `geo`) values ("""+'"'+str(niveles[2]['nombre'])+'"'+', '+str(niveles[1]['pk'])+', '+str(2)+');'
			f.write(c)
			f.write('\n')
			# ==================================
			for niveles[3] in niveles[2]['municipio']:
				#c = """insert into `geo_municipio` (`id`, `nombre`, `sup`, `geo`) values ("""+str(niveles[3]['pk'])+', "'+str(niveles[3]['nombre'])+'"'+', '+str(niveles[2]['pk'])+', '+str(3)+');'
				key_municipio = key_municipio + 1
				c = """insert into `geo_municipio` (`nombre`, `sup`, `geo`) values ("""+'"'+str(niveles[3]['nombre'])+'"'+', '+str(key_provincia)+', '+str(3)+');'
				f.write(c)
				f.write('\n')
				# ==================================
				for niveles[4] in niveles[3]['localidad']:
					#c = """insert into `geo_localidad` (`id`, `nombre`, `sup`, `geo`) values ("""+str(niveles[4]['pk'])+', "'+str(niveles[4]['nombre'])+'"'+', '+str(niveles[3]['pk'])+', '+str(4)+');'
					c = """insert into `geo_localidad` (`id`, `nombre`, `sup`, `geo`) values ("""+str(niveles[4]['pk'])+', "'+str(niveles[4]['nombre'])+'"'+', '+str(key_municipio)+', '+str(4)+');'
					if (niveles[4]['nombre'] == 'Santa Cruz de la Sierra'):
						print (c)
					f.write(c)
					f.write('\n')
					key_localidad = key_localidad + 1
					# ==================================
					for niveles[5] in niveles[4]['recinto']:
						#c = """insert into `geo_recinto` (`id`, `nombre`, `sup`, `geo`) values ("""+str(niveles[5]['pk'])+', "'+str(niveles[5]['nombre'])+'"'+', '+str(niveles[4]['pk'])+', '+str(5)+');'
						c = """insert into `geo_recinto` (`nombre`, `sup`, `geo`) values ("""+'"'+str(niveles[5]['nombre'])+'"'+', '+str(niveles[4]['pk'])+', '+str(5)+');'
						key_recinto = key_recinto + 1
						#c = """insert into `geo_recinto` (`nombre`, `sup`, `geo`) values ("""+'"'+str(niveles[5]['nombre'])+'"'+', '+str(key_localidad)+', '+str(5)+');'
						if (niveles[5]['nombre'] == 'Campus Universitario'):
							print (c)
						f.write(c)
						f.write('\n')
						# ==================================
						for niveles[6] in niveles[5]['mesa']:
							#c = """insert into `geo_mesa` (`id`, `nombre`, `sup`, `geo`) values ("""+str(niveles[6]['pk'])+', "'+str(niveles[6]['nombre'])+'"'+', '+str(niveles[5]['pk'])+', '+str(5)+');'
							c = """insert into `geo_mesa` (`id`, `nombre`, `sup`, `geo`) values ("""+str(niveles[6]['pk'])+', "'+str(niveles[6]['nombre'])+'"'+', '+str(key_recinto)+', '+str(5)+');'
							if (niveles[6]['pk'] == 70009):
								print (c)
							f.write(c)
							f.write('\n')
print ('****************************')
print (key_provincia, 'key_provincia')						
print (key_municipio, 'key_municipio')
print (key_localidad, 'key_localidad')
print (key_recinto, 'geo_recinto')
f.close()