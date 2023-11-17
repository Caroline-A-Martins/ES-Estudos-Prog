"""form math import radians, sim, cos, tan
depois apagar os math's do codigo"""
import math
ang = float(input('Digite o angulo que você deseja: '))
print(ang)
seno = math.sin(math.radians(ang))
print('O angulo de {} tem o SENO de {:.2f} '.format(ang, seno))
cos = math.cos(math.radians(ang))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tang = math.tan(math.radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tang))
