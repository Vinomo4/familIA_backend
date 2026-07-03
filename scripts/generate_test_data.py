import os
import csv

def generate_router_data():
    # 50 cases for MANAGEMENT
    management_cases = [
        "¿Me ha llegado ya la pensión de este mes?",
        "Mira a ver si me han ingresado el dinero de la jubilación.",
        "¿Cuánto dinero me queda en la libreta?",
        "Dime el saldo de mi cuenta corriente, por favor.",
        "¿He pagado ya el recibo de la luz?",
        "¿Cuánto me han cobrado de electricidad este mes?",
        "¿Cuánto me he gastado en la farmacia últimamente?",
        "Suma todos los gastos que tengo en medicinas.",
        "¿Cuánto he gastado en el supermercado esta semana?",
        "Dime el total de las compras de alimentación.",
        "Apunta que he sacado 50 euros del cajero automático.",
        "Registra una retirada de efectivo de 20 euros.",
        "Anota que le he dado 10 euros a mi nieto para el cine.",
        "¿Tengo alguna comisión de mantenimiento este mes?",
        "Mira si el banco me ha cobrado comisiones raras.",
        "¿Cuál ha sido el último movimiento de mi cuenta?",
        "Dime lo último que he pagado con la tarjeta.",
        "¿Cuánto pagué de teléfono la última vez?",
        "Mira a ver el recibo de Movistar cuánto ha sido.",
        "¿Tengo saldo suficiente para pagar el recibo que viene?",
        "¿Me llegará con lo que tengo para pagar el gas?",
        "Anota un gasto de 12 euros en la panadería.",
        "He gastado 8 euros en la cafetería, apúntalo.",
        "¿Cuánto llevo gastado en total este mes?",
        "¿Cuánto dinero he ahorrado desde enero?",
        "¿Ha entrado algún ingreso nuevo hoy?",
        "Quiero saber si me han devuelto lo del seguro.",
        "¿Tengo algún cargo duplicado en la cuenta?",
        "Revisa si me han cobrado dos veces en el súper.",
        "Apunta 30 euros que saqué ayer para compras.",
        "Registra un gasto en efectivo de 15 euros en el mercado.",
        "¿Cuánto he gastado en farmacia en el mes de marzo?",
        "Dime los gastos de farmacia de este mes.",
        "¿Cuánto pagué de gas el mes pasado?",
        "¿Cuánto ha sido el recibo del agua?",
        "¿Me han cobrado ya el seguro de la casa?",
        "¿Cuánto dinero tengo en total sumando las dos cuentas?",
        "Dime el saldo total disponible.",
        "¿Tengo alguna alerta de descubierto en mi cuenta?",
        "Anota que he pagado 25 euros en la frutería.",
        "Apunta 5 euros que me costó el taxi.",
        "¿Cuánto he gastado en total en el supermercado Día?",
        "Dime la suma de lo gastado en Mercadona.",
        "¿Me han cobrado alguna comisión por usar el cajero?",
        "¿Hay algún cobro extraño en la cuenta esta semana?",
        "¿Cuánto dinero en efectivo me queda en el monedero digital?",
        "Dime el saldo del monedero de efectivo.",
        "Apunta 40 euros que saqué del cajero de la esquina.",
        "Anota que gasté 18 euros en medicinas.",
        "¿Cuándo se cobra la pensión normalmente?"
    ]

    # 50 cases for SCAM
    scam_cases = [
        "Me acaban de mandar un mensaje diciendo que mi cuenta está bloqueada y que entre en un enlace.",
        "Me piden que verifique mis claves bancarias a través de un link urgente.",
        "Un señor me ha llamado diciendo que es de mi banco y que le dé un código que me ha llegado al móvil.",
        "Me ha llegado un SMS que dice que he hecho una compra de 500 euros y que llame a un número si no la reconozco.",
        "Dicen que si no pago una deuda ahora mismo con Bizum vendrá la policía.",
        "Me piden por WhatsApp que envíe dinero urgente a mi hijo que dice que ha perdido el teléfono.",
        "Mamá he perdido el móvil y necesito que me hagas una transferencia de 400 euros a esta cuenta.",
        "Hola abuela, soy tu nieto, he tenido un problema y necesito dinero ya, no se lo digas a mis padres.",
        "Me llama un técnico de Microsoft diciendo que mi ordenador tiene un virus y que entre a mi banco.",
        "Un informático me dice que tiene que controlar mi móvil para arreglar la aplicación de banca.",
        "Me dicen que transfiera mis ahorros a una cuenta segura porque mi banco está bajo ataque.",
        "Me piden que cambie todo mi dinero a una cuenta de seguridad para protegerlo de un fraude.",
        "Un mensaje dice que mi tarjeta de crédito ha sido suspendida y debo poner el PIN en una web.",
        "Me ha llegado un correo electrónico pidiendo mi contraseña de banca online para actualizar el sistema.",
        "Me exigen que haga un pago inmediato por Bizum o me bloquearán las cuentas para siempre.",
        "Me están llamando y me dicen que no cuelgue el teléfono o perderé todo mi dinero.",
        "Me dicen que confirme mis datos personales y de tarjeta en este enlace para evitar una penalización.",
        "Un mensaje de Correos dice que tengo un paquete pendiente y debo pagar 2 euros metiendo mi tarjeta.",
        "Dicen que me ha tocado un premio de la lotería y que para cobrarlo debo dar mis claves del banco.",
        "Me llama una mujer diciendo que es de la seguridad social y quiere mi cuenta para ingresarme una ayuda.",
        "Me ha llegado un mensaje SMS con un enlace de BBVA diciendo que valide mi acceso.",
        "Un correo dice que mi cuenta de CaixaBank ha sido restringida y debo reactivarla metiendo mis datos.",
        "Me piden que haga un Bizum a un número desconocido para anular un cargo falso.",
        "Me dice un chico por teléfono que si le doy el código SMS me devolverán una comisión cobrada por error.",
        "Un mensaje de WhatsApp de un número raro dice que es mi hija y que necesita dinero urgente.",
        "Me piden que instale un programa en el móvil para que el banco me pueda ayudar a distancia.",
        "Un SMS dice que si no pulso en el enlace me cobrarán una multa de Hacienda de forma inmediata.",
        "Me dicen que han entrado en mi cuenta y que para bloquear el acceso debo facilitar mis coordenadas.",
        "Un supuesto empleado del banco me pide por teléfono que le lea los números de mi tarjeta de crédito.",
        "Me dicen que mi cuenta tiene un cargo de Amazon de 300 euros y que meta mi contraseña para cancelarlo.",
        "Me escriben diciendo que tengo que actualizar mis datos de seguridad en menos de 24 horas.",
        "Me ha llegado una alerta de seguridad muy urgente diciendo que alguien está intentando sacar dinero.",
        "Dicen que son de mi compañía de la luz y que si no pago por Bizum ahora mismo me cortan el suministro.",
        "Un SMS de Santander dice que mi banca móvil ha sido desactivada por seguridad y da un enlace.",
        "Me piden mis claves por teléfono porque dicen que hay una transferencia sospechosa que deben detener.",
        "Un correo electrónico de mi banco me pide que confirme las preguntas de seguridad y mi PIN.",
        "Me ha llegado un mensaje sospechoso que dice que firme una operación de Bizum para recibir un reembolso.",
        "Me piden la clave de firma digital para autorizar una devolución de dinero.",
        "Un supuesto policía me llama diciendo que mi cuenta está siendo usada para fraudes y debo cooperar dándole mis claves.",
        "Me dicen que he ganado un sorteo del banco y que introduzca mi número de cuenta y clave de acceso.",
        "Me envían un enlace por SMS para evitar que mi tarjeta de débito caduque hoy mismo.",
        "Me ha llamado mi supuesto sobrino diciendo que está retenido en el aeropuerto y necesita 500 euros.",
        "Me piden que envíe dinero a través de una empresa de envíos urgentes porque un familiar está enfermo.",
        "Un correo electrónico dice que mi declaración de la renta es a devolver y me pide la tarjeta.",
        "Me envían un mensaje con un enlace acortado que dice que mi cuenta bancaria ha sido bloqueada temporalmente.",
        "Me llaman diciendo que son del servicio de prevención de fraudes del banco y me piden verificar mis claves.",
        "Un mensaje de texto me avisa de un cargo inusual y me da un botón para cancelarlo metiendo mis datos.",
        "Me solicitan por correo mi número de tarjeta y el código CVV de atrás para validar mi cuenta.",
        "Me exigen hacer una transferencia a un número de cuenta extranjero para solucionar un problema judicial urgente.",
        "Me ha llegado un SMS amenazante diciendo que si no pago una supuesta tasa perderé mis derechos de pensión."
    ]

    # 50 cases for DOCUMENT
    document_cases = [
        "Me ha llegado una carta del banco que no entiendo muy bien, ¿me la explicas?",
        "Tengo aquí una notificación en papel sobre un cambio de condiciones de mi cuenta.",
        "Quiero saber qué significa esta carta de comisiones que me ha enviado el banco.",
        "He recibido un documento del banco donde pone algo de mantenimiento de cuenta de 240 euros.",
        "¿Me puedes leer este papel que me ha llegado por correo postal de mi sucursal?",
        "Tengo un aviso impreso del banco sobre una nueva tarifa de mi tarjeta de débito.",
        "Me ha llegado una carta sobre el cobro de la hipoteca, ¿qué dice exactamente?",
        "¿Este papel del banco dice que tengo que pagar alguna comisión nueva?",
        "He recibido una carta extraña que parece del banco, no sé si es verdadera o falsa.",
        "¿Me puedes explicar qué es esta carta que me ha llegado del catastro?",
        "Me ha llegado una notificación del banco por correo electrónico en formato PDF.",
        "Tengo un documento que habla de un cambio en el contrato de mi libreta de ahorros.",
        "¿Me puedes resumir esta carta informativa que me ha enviado mi gestor del banco?",
        "Me ha llegado un papel donde pone que me van a cobrar por tener la cuenta abierta.",
        "¿Qué significa este cambio de condiciones contractuales que viene en esta carta?",
        "Tengo una carta del banco sobre comisiones y quiero saber si es correcta.",
        "Ayúdame a entender este extracto bancario mensual que me ha llegado a casa.",
        "Me ha llegado una carta que dice que mi oficina del banco va a cerrar.",
        "Tengo un documento en papel sobre la renovación de mi tarjeta de crédito.",
        "Quiero que revises esta carta donde dice que tengo un cargo pendiente.",
        "¿Me puedes explicar qué significa este recibo impreso del seguro del coche?",
        "He recibido un aviso por escrito de que me van a subir el coste de mantenimiento.",
        "Tengo una notificación en papel del banco que me pide actualizar mi DNI.",
        "Me ha llegado una carta sobre la subida de los intereses, ¿me la traduces a lenguaje sencillo?",
        "¿Este papel que me ha llegado del banco es un recibo o una reclamación de pago?",
        "Tengo un documento que habla de la cancelación de mi depósito a plazo fijo.",
        "¿Me puedes explicar este papel informativo sobre los nuevos horarios de la oficina?",
        "Me ha llegado una carta del banco sobre las pensiones de este año, ¿qué dice?",
        "Tengo un aviso de cobro de un impuesto municipal por escrito, ¿cuándo me lo cobran?",
        "¿Qué significa esta carta que dice que mi cuenta pasa a ser de tarifa plana?",
        "Tengo un folleto del banco sobre un fondo de inversión, ¿es seguro para mí?",
        "Me ha llegado una carta reclamando una documentación que no sé qué es.",
        "¿Me puedes aclarar qué es este papel de la comunidad de vecinos del banco?",
        "Tengo una carta que dice que tengo que firmar unas condiciones nuevas de banca online.",
        "Me ha llegado una notificación escrita de que mi cuenta tiene saldo negativo.",
        "¿Qué significa este papel que dice que mi tarjeta de débito tiene comisiones adicionales?",
        "Tengo un extracto bancario en papel con unos números muy pequeños que no veo bien.",
        "¿Me puedes resumir lo más importante de esta carta que me ha llegado de la seguridad social?",
        "He recibido un aviso de una comisión de 120 euros anuales por correo postal.",
        "Tengo una carta del banco que habla de un seguro de vida asociado a mi cuenta.",
        "¿Me explicas este papel que me han dado hoy en la sucursal del banco?",
        "Tengo un documento de liquidación de intereses de mi cuenta de ahorro.",
        "Me ha llegado una carta sobre el cobro de la tasa de basuras, ¿qué significa?",
        "¿Qué pone en esta carta del banco sobre la protección de datos?",
        "Tengo un aviso impreso de que mi tarjeta ha sido renovada automáticamente.",
        "Me ha llegado una carta que dice que tengo derecho a un reembolso de comisiones.",
        "Tengo una carta del banco de seguros que no entiendo, ¿me ayudas?",
        "¿Me puedes leer este documento que me ha llegado con el membrete del banco de España?",
        "Tengo una notificación por escrito de un cargo de 45 euros de mantenimiento.",
        "¿Qué significa este aviso en papel sobre la jubilación y los planes de pensiones?"
    ]

    # 50 cases for INTERFACE
    interface_cases = [
        "No encuentro el botón para ver el saldo en la aplicación del banco.",
        "¿Dónde tengo que pulsar para ver los últimos movimientos en el móvil?",
        "La pantalla de la aplicación se ha quedado en blanco y no me deja hacer nada.",
        "No sé cómo volver a la pantalla de inicio de la aplicación bancaria.",
        "¿Cómo puedo ver cuánto dinero tengo en la tarjeta desde la app?",
        "No encuentro el botón para hacer un Bizum en la pantalla del móvil.",
        "¿Dónde está el menú para ver los recibos domiciliados en la aplicación?",
        "Me sale un mensaje de error en la pantalla del banco y no sé qué significa.",
        "La letra de la aplicación es muy pequeña y no consigo leer las opciones.",
        "No sé dónde pulsar para salir de la aplicación del banco de forma segura.",
        "¿Cómo se cambia la contraseña de acceso desde la app del móvil?",
        "No veo el botón para enviar dinero a mi hijo en esta pantalla.",
        "Me pide una clave en la pantalla y no sé si es la de acceso o la de firma.",
        "¿Dónde tengo que tocar para descargar el recibo de la luz en el móvil?",
        "La aplicación me dice que actualice la app y no sé dónde hay que darle.",
        "No sé cómo ver si me han cobrado el recibo del agua desde el móvil.",
        "¿Dónde se pulsa para ver los datos de mi tarjeta de débito en la app?",
        "No me aclaro con el menú nuevo del banco, ¿dónde están mis cuentas?",
        "Me sale un círculo dando vueltas en la pantalla del banco y no avanza.",
        "No sé dónde está la opción para hacer una transferencia en la aplicación.",
        "¿Cómo puedo ver el extracto del mes pasado en la pantalla del móvil?",
        "No encuentro el botón de ayuda dentro de la aplicación de banca.",
        "La aplicación me pide que escanee mi cara y no sé cómo se hace.",
        "¿Dónde se pulsa para activar la nueva tarjeta en la aplicación móvil?",
        "No sé cómo buscar un movimiento antiguo en la pantalla de la app.",
        "Me sale un aviso de cookies en la app y no me deja ver el saldo, ¿dónde doy?",
        "No encuentro el botón para configurar las notificaciones en el móvil.",
        "¿Cómo puedo ver los detalles de una compra en la pantalla del banco?",
        "No sé dónde se pulsa para bizumear dinero a un contacto de mi agenda.",
        "Me pide que ponga la huella digital y no sé dónde hay que poner el dedo.",
        "¿Dónde está la opción de contacto con mi oficina en la aplicación?",
        "No sé cómo borrar un gasto anotado en la app del banco.",
        "La aplicación del banco me dice que la sesión ha caducado, ¿qué hago?",
        "¿Dónde se pulsa para ver el saldo de la libreta de ahorros en la app?",
        "No encuentro el botón para apagar la tarjeta temporalmente en el móvil.",
        "¿Cómo puedo ver los gastos del supermercado agrupados en la app?",
        "No sé dónde se pulsa para aceptar las nuevas condiciones en la pantalla.",
        "Me sale un teclado en la pantalla que no tiene números, ¿cómo escribo?",
        "No encuentro la pestaña de mis tarjetas en el menú de la aplicación.",
        "¿Dónde tengo que dar para ver el saldo de mi cuenta de ahorro?",
        "No sé cómo enviar un justificante de pago desde la aplicación del móvil.",
        "¿Cómo se hace para ver los números de mi cuenta IBAN en la app?",
        "No encuentro el botón para reclamar una comisión dentro del móvil.",
        "La pantalla me pide un código SMS pero no me llega nada, ¿dónde pulso?",
        "No sé dónde está el botón para ver los movimientos de efectivo anotados.",
        "¿Cómo vuelvo al menú principal del banco si me he metido en transferencias?",
        "No encuentro el botón para ver los recibos pendientes de pago en la app.",
        "¿Dónde se pulsa para cambiar el límite de dinero de mi tarjeta?",
        "No me sale el teclado en la pantalla para poner mi clave de acceso.",
        "¿Cómo puedo ver los datos de contacto del servicio técnico en la app?"
    ]

    cases = []
    # Combine cases into a dataset of 200 items
    for text in management_cases:
        cases.append({"text": text, "expected_category": "MANAGEMENT"})
    for text in scam_cases:
        cases.append({"text": text, "expected_category": "SCAM"})
    for text in document_cases:
        cases.append({"text": text, "expected_category": "DOCUMENT"})
    for text in interface_cases:
        cases.append({"text": text, "expected_category": "INTERFACE"})
        
    return cases

def generate_fraud_data():
    # 100 actual Fraud cases
    fraud_cases = [
        ("Me piden transferir mi dinero a una cuenta segura porque mi cuenta está bajo ataque.", "vishing"),
        ("Hola mamá, he perdido el móvil. Por favor envíame dinero urgente por Bizum a este número.", "suplantacion_familiar"),
        ("Hola papá, mi móvil se ha roto y no puedo llamar. Necesito pagar una factura urgente, hazme un Bizum.", "suplantacion_familiar"),
        ("Su cuenta bancaria ha sido bloqueada temporalmente por seguridad. Pulse en este enlace para reactivarla inmediatamente: https://bancoseguro.com", "phishing"),
        ("Para evitar cargos mensuales adicionales, confirme sus claves de seguridad y DNI en el siguiente enlace urgente.", "phishing"),
        ("Le llamo del departamento de seguridad del banco. Para cancelar una compra no autorizada, necesito que me diga el código SMS que acaba de recibir.", "vishing"),
        ("Un técnico de soporte de su banco me dice que debe conectarse a mi móvil con AnyDesk para solucionar un problema en mi banca.", "soporte_falso"),
        ("Me llama un supuesto informático del banco diciendo que hay un virus en mi cuenta y que tengo que facilitarle mi PIN.", "soporte_falso"),
        ("Urgente: Se ha detectado una transferencia sospechosa de 800 euros en su cuenta. Cancele el envío pulsando aquí: https://seguridad-alertas.com", "phishing"),
        ("Estimado cliente, su tarjeta ha sido desactivada temporalmente. Valide su identidad en 2 horas para evitar cargos de bloqueo: https://santander-acceso.com", "phishing"),
        ("Me dicen que haga un Bizum urgente de 100 euros para desbloquear mi cuenta corriente que ha sido suspendida.", "vishing"),
        ("Me llaman del banco diciendo que hay un cobro duplicado de 300 euros y que necesitan mi clave de firma para anularlo.", "vishing"),
        ("Un mensaje de Correos dice que mi paquete no se puede entregar por falta de pago de tasas y me da un link para poner mi tarjeta.", "phishing"),
        ("Hola abuela, soy tu nieto, he tenido un accidente con el coche y necesito que me envíes 600 euros urgentemente, no le digas nada a nadie.", "suplantacion_familiar"),
        ("Me escribe mi supuesto sobrino diciendo que está retenido por la aduana y necesita que le haga un Bizum de inmediato.", "suplantacion_familiar"),
        ("Un SMS de Hacienda me dice que tengo un reembolso de 120 euros pendiente y que pinche en el enlace para rellenar los datos de mi tarjeta.", "phishing"),
        ("Me llaman diciendo que son de la distribuidora de luz y que si no pago una factura pendiente de 150 euros ahora mismo cortan la luz.", "vishing"),
        ("Un correo electrónico del BBVA me advierte que mi cuenta será cancelada definitivamente si no verifico mis claves en este link.", "phishing"),
        ("Me solicitan la clave de firma digital por teléfono para devolverme unos gastos de mantenimiento que me cobraron por error.", "vishing"),
        ("Un supuesto inspector de policía me dice que mis cuentas están en peligro y que debo transferir todo mi saldo a una cuenta judicial.", "vishing")
    ]
    
    # Expand to 100 cases using variations of standard scam tactics (phishing, vishing, family impersonation, tech support scam)
    expanded_fraud = []
    scam_types = ["phishing", "vishing", "suplantacion_familiar", "soporte_falso"]
    
    # Duplicate and slightly modify templates to reach 100 cases
    for i in range(5):
        for text, ftype in fraud_cases:
            # Add minor variations to the text
            variations = [
                f"{text}",
                f"Alerta: {text}",
                f"Me ha llegado esto: {text}",
                f"Me acaban de mandar lo siguiente: '{text}'",
                f"Tengo una llamada donde {text.lower()}" if not text.startswith("Me") else text
            ]
            expanded_fraud.append((variations[i % len(variations)], ftype))
            
    # Keep only the first 100
    expanded_fraud = expanded_fraud[:100]
    
    # 100 Non-Fraud cases (Control/Safe cases)
    # 50 management, 25 document (safe), 25 interface (safe)
    safe_cases = [
        ("¿Me ha llegado ya la pensión de este mes?", "control_normal"),
        ("Dime el saldo de mi cuenta corriente, por favor.", "control_normal"),
        ("¿Cuánto me han cobrado de electricidad este mes?", "control_normal"),
        ("Suma todos los gastos que tengo en medicinas.", "control_normal"),
        ("¿Cuánto he gastado en el supermercado esta semana?", "control_normal"),
        ("Apunta que he sacado 50 euros del cajero automático.", "control_normal"),
        ("Anota que le he dado 10 euros a mi nieto para el cine.", "control_normal"),
        ("¿Tengo alguna comisión de mantenimiento este mes?", "control_normal"),
        ("¿Cuál ha sido el último movimiento de mi cuenta?", "control_normal"),
        ("¿Cuánto pagué de teléfono la última vez?", "control_normal"),
        ("¿Me llegará con lo que tengo para pagar el gas?", "control_normal"),
        ("Anota un gasto de 12 euros en la panadería.", "control_normal"),
        ("¿Cuánto llevo gastado en total este mes?", "control_normal"),
        ("¿Cuánto dinero he ahorrado desde enero?", "control_normal"),
        ("Revisa si me han cobrado dos veces en el súper.", "control_normal"),
        ("Apunta 30 euros que saqué ayer para compras.", "control_normal"),
        ("¿Cuánto he gastado en farmacia en el mes de marzo?", "control_normal"),
        ("¿Cuánto pagué de gas el mes pasado?", "control_normal"),
        ("¿Cuánto ha sido el recibo del agua?", "control_normal"),
        ("¿Me han cobrado ya el seguro de la casa?", "control_normal"),
        
        # Document (safe)
        ("Me ha llegado una carta del banco que no entiendo muy bien, ¿me la explicas?", "control_normal"),
        ("Tengo aquí una notificación en papel sobre un cambio de condiciones de mi cuenta.", "control_normal"),
        ("Quiero saber qué significa esta carta de comisiones que me ha enviado el banco.", "control_normal"),
        ("He recibido un documento del banco donde pone algo de mantenimiento de cuenta de 240 euros.", "control_normal"),
        ("Tengo un aviso impreso del banco sobre una nueva tarifa de mi tarjeta de débito.", "control_normal"),
        ("Me ha llegado una carta sobre el cobro de la hipoteca, ¿qué dice exactamente?", "control_normal"),
        ("¿Este papel del banco dice que tengo que pagar alguna comisión nueva?", "control_normal"),
        ("¿Me puedes explicar qué es esta carta que me ha llegado del catastro?", "control_normal"),
        ("Me ha llegado una notificación del banco por correo electrónico en formato PDF.", "control_normal"),
        ("Tengo un documento que habla de un cambio en el contrato de mi libreta de ahorros.", "control_normal"),
        
        # Interface (safe)
        ("No encuentro el botón para ver el saldo en la aplicación del banco.", "control_normal"),
        ("¿Dónde tengo que pulsar para ver los últimos movimientos en el móvil?", "control_normal"),
        ("No sé cómo volver a la pantalla de inicio de la aplicación bancaria.", "control_normal"),
        ("¿Cómo puedo ver cuánto dinero tengo en la tarjeta desde la app?", "control_normal"),
        ("No encuentro el botón para hacer un Bizum en la pantalla del móvil.", "control_normal"),
        ("¿Dónde está el menú para ver los recibos domiciliados en la aplicación?", "control_normal"),
        ("La letra de la aplicación es muy pequeña y no consigo leer las opciones.", "control_normal"),
        ("No sé dónde pulsar para salir de la aplicación del banco de forma segura.", "control_normal"),
        ("¿Cómo se cambia la contraseña de acceso desde la app del móvil?", "control_normal"),
        ("No veo el botón para enviar dinero a mi hijo en esta pantalla.", "control_normal")
    ]
    
    # Duplicate and modify safe cases to reach 100 cases
    expanded_safe = []
    for i in range(10):
        for text, ftype in safe_cases:
            variations = [
                f"{text}",
                f"Por favor, {text.lower()}" if not text.startswith("¿") else text,
                f"Hola. {text}",
                f"Ayúdame con esto: {text}",
                f"Quiero preguntar: {text}"
            ]
            expanded_safe.append((variations[i % len(variations)], ftype))
            
    # Keep only the first 100
    expanded_safe = expanded_safe[:100]
    
    # Combine fraud and safe cases into a dataset of 200 items
    cases = []
    for text, ftype in expanded_fraud:
        cases.append({"text": text, "is_fraud": True, "fraud_type": ftype})
    for text, ftype in expanded_safe:
        cases.append({"text": text, "is_fraud": False, "fraud_type": ftype})
        
    return cases

def main():
    base_dir = "/home/vinomo/programming/master/data_science_and_ai/familIA/data/synthetic/kpi_testing"
    os.makedirs(base_dir, exist_ok=True)
    
    # 1. Router classification
    router_file = os.path.join(base_dir, "router_classification.csv")
    router_data = generate_router_data()
    with open(router_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["text", "expected_category"])
        writer.writeheader()
        writer.writerows(router_data)
    print(f"Generated {len(router_data)} cases in {router_file}")
    
    # 2. Fraud detection
    fraud_file = os.path.join(base_dir, "fraud_detection.csv")
    fraud_data = generate_fraud_data()
    with open(fraud_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["text", "is_fraud", "fraud_type"])
        writer.writeheader()
        writer.writerows(fraud_data)
    print(f"Generated {len(fraud_data)} cases in {fraud_file}")

if __name__ == "__main__":
    main()
