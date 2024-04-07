
import random

adjectives = ["Cool", "Mystic", "Electric", "Wild", "Groovy", "ghost","magico"
,"fuego","hola" ,"adios","persona","gente","hombre","mujer","bebe","bolsa","triste"            
,"amor","flores","rosa","dinero","arriba","abajo","corrido","celular","vape","fresa" 
,"azul","verde","tamal de rajas","fernado6752","god918","celular.verde","rafa9284"
,"cartera.qro523","raton,vaquero7883","carton_mojado","fornite763","omega_dif"
,"cielito_azul","arreglo_de_pc","esculadefornite","gimacion_god6123","dinero_falso"             
,"faze_clan736","conexion _rapidadeinternet","personas_negras","coca_en_bolsa"             
,"refrescoblanco","perfumesdecolor","las_mejores_plumas","dentista","papelesdecolores"             
,"librosdecalculo32","camas_matrimoniales","puertas_de_metal","camaras_de_seguridad"             
,"sillas_de_madera","monitores213hrz","calculadoras rapidas","gorras_def1","cuadros_de_flores"             
,"dedos_de_queso1873","palomitasde_sabor6723","adopta_perros2867","aromatisantes8673"
,"internet_rapido267","usuario_de_pc873","puesto_abierto98","democratico.hola","error,gg"
,"elfuturo,es,hoy","muchos,perros","campana,dorada","estudios,rapidos","fuerza_suprema"
,"monstruo_feo","sayayin873","elmejor","entrenador_personal","planeta_dios","universo"
,"construccion_de_casas","problemita_feo","anngel928","luz_liminosa","halmuada_comada"
,"ki_dibino","vegetta9948","monedas_fake","pastel_rosa","desodorante_fresco","mocilas_grandes"
,"pintor_de_paderes","cables_largos","maus_gamer","haker928","pepito768","igualdad_de_genero"
,"machismo850","soy_gay","el-feo923","pepinillo90","ratita7","the_bos","fok_boy","sad874"
,"soporte_de_teles","expulsion764","cabello_gris","poder_devastador","eldevoradordemundos"
]

nouns = ["gmail","hotmail","yahoo","outlook"]

def generate_band_name():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective}@{noun}.com"

band_name = generate_band_name()
print(band_name)
