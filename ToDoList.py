from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import mysql.connector
import time
import threading
from datetime import date
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk



# Crea la ventana principal
Principal = tk.Tk()
Principal.title("ToDoList")
# Obtiene el ancho y alto de la pantalla
screen_width = Principal.winfo_screenwidth()
screen_height = Principal.winfo_screenheight()
Principal.geometry(f"{screen_width}x{screen_height}")
Principal.grid_columnconfigure(0, minsize=100)
Principal.grid_rowconfigure(0, minsize=100)
#Principal.columnconfigure(0, weight=1)
#Principal.attributes("-fullscreen", True)



def abrir_ventana():
    # Crear la segunda ventana
    Nueva_Tarea = tk.Tk()
    Nueva_Tarea.title('Ventana secundaria')
    Nueva_Tarea.geometry("325x600")
    Nueva_Tarea.grid_columnconfigure(0, minsize=50)
    Nueva_Tarea.grid_rowconfigure(0, minsize=50)


    label = tk.Label(Nueva_Tarea, text="Escribe el titulo de la tarea:")
    label.grid(row=0, column=0)
    # Crea el textbox
    textboxtitle = tk.Text(Nueva_Tarea)
    # Establece el ancho y alto del textbox en 10 caracteres
    textboxtitle.config(width=40, height=1)
    # Empaqueta el textbox en la ventana principal
    textboxtitle.grid(row=1, column=0)


    label = tk.Label(Nueva_Tarea, text="Escribe la descripción de la tarea:")
    label.grid()
    # Crea el textbox
    textboxdes = tk.Text(Nueva_Tarea)
    # Establece el ancho y alto del textbox en 10 caracteres
    textboxdes.config(width=40, height=5)
    # Empaqueta el textbox en la ventana principal
    textboxdes.grid()


    label = tk.Label(Nueva_Tarea, text="Selecciona la prioridad de la tarea:")
    label.grid()
    # Crea una lista de opciones para el combobox
    options = ["Prioridad maxima", "Prioridad media", "Prioridad baja"]
    # Crea el combobox y lo empaqueta
    comboboxpriority = ttk.Combobox(Nueva_Tarea, values=options)
    comboboxpriority.config(state="readonly")
    comboboxpriority.grid()



    label = tk.Label(Nueva_Tarea, text="Selecciona el tiempo estimado para completar la tarea:")
    label.grid()
    # Crea una lista de opciones para el combobox
    options = ["10 minutos", "15 minutos", "30 minutos", "1 hora"]
    # Crea el combobox y lo empaqueta
    comboboxtime = ttk.Combobox(Nueva_Tarea, values=options)
    comboboxtime.config(state="readonly")
    comboboxtime.grid()


    label = tk.Label(Nueva_Tarea, text="Selecciona la fecha limite para completar la tarea:")
    label.grid()
    # Crea una lista de opciones para el combobox
    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    # Crea el combobox y lo empaqueta
    comboboxdate1 = ttk.Combobox(Nueva_Tarea, values=options)
    comboboxdate1.config(state="readonly")
    comboboxdate1.grid()

    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    # Crea el combobox y lo empaqueta
    comboboxdate2 = ttk.Combobox(Nueva_Tarea, values=options)
    comboboxdate2.config(state="readonly")
    comboboxdate2.grid()

    options = ["2022", "2023", "2024", "2025"]
    # Crea el combobox y lo empaqueta
    comboboxdate3 = ttk.Combobox(Nueva_Tarea, values=options)
    comboboxdate3.config(state="readonly")
    comboboxdate3.grid()


    def show_reminder():
        # Muestra el recordatorio en una ventana emergente
        messagebox.showinfo("Recordatorio", "¡No olvides hacer tu tarea:!")

    class ReminderThread(threading.Thread):
        def __init__(self, horas, minutos):
            self.horas = horas
            self.minutos = minutos
            super().__init__()

        def run(self):
            # Obtiene la hora actual
            current_time = time.localtime()
            # Calcula cuántos segundos faltan para que se cumpla la hora especificada
            seconds_left = (self.horas - current_time.tm_hour) * 3600 + (self.minutos - current_time.tm_min) * 60 - current_time.tm_sec
            # Detiene la ejecución del programa durante los segundos calculados
            time.sleep(seconds_left)
            # Muestra el recordatorio
            show_reminder()

    label = tk.Label(Nueva_Tarea, text="Introduce la hora del recordatorio (0-23):")
    label.grid()
    # Crea una lista de opciones para el combobox
    options = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
    # Crea el combobox y lo empaqueta
    comboboxhoras = ttk.Combobox(Nueva_Tarea, values=options)
    comboboxhoras.config(state="readonly")
    comboboxhoras.grid()

    label = tk.Label(Nueva_Tarea, text="Introduce los minutos del recordatorio (0-59):")
    label.grid()
    # Crea una lista de opciones para el combobox
    options = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"
    ,"31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
    # Crea el combobox y lo empaqueta
    comboboxminutos = ttk.Combobox(Nueva_Tarea, values=options)
    comboboxminutos.config(state="readonly")
    comboboxminutos.grid()    

    def ingresar_datos():

        
        titulo = textboxtitle.get("1.0", "end")
        descripcion = textboxdes.get("1.0", "end")
        prioridad = comboboxpriority.get()
        tiempoestimado = comboboxtime.get()
        fechalimite1 = comboboxdate1.get()
        fechalimite2 = comboboxdate2.get()
        fechalimite3 = comboboxdate3.get()
        fechalimite = fechalimite1+"/"+fechalimite2+"/"+fechalimite3
        horas = int(comboboxhoras.get())
        minutos = int(comboboxminutos.get())
        horas = horas
        minutos = minutos


        # Conecta a la base de datos
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="to_do_list"
        )
        # Crea un cursor
        cursor = conn.cursor()
        # Ejecuta una consulta de inserción
        cursor.execute("INSERT INTO to_do_list.tareas (Titulo, Descripcion, Prioridad, FechaLimite, TiempoEstimado) VALUES (%s, %s, %s, %s, %s)", (titulo, descripcion, prioridad, tiempoestimado, fechalimite))
        # Asegúrate de hacer commit de los cambios
        conn.commit()
        # Cierra la conexión
        conn.close()

        thread = ReminderThread(horas, minutos)
        thread.start()

        """
        if horas or minutos == "":
            print("no recordatorio")
        else:
             #Crea una instancia de ReminderThread y la ejecuta en un hilo en segundo plano
            thread = ReminderThread(horas, minutos)
            thread.start()
        """

        Nueva_Tarea.destroy()
        actualizar()
        


    button = tk.Button(Nueva_Tarea, text="Crear nueva tarea", command = ingresar_datos)
    button.grid()


def buscar():

    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="to_do_list"
    )
    cursor = cnx.cursor()

    valor_buscar = textboxsearch.get("1.0", "end")
    cursor.execute("SELECT * FROM tareas WHERE titulo = '" + valor_buscar + "' OR descripcion = '" + valor_buscar + "'")
    result = cursor.fetchall()

    if len(result) > 0:
        Busqueda_ventana = tk.Toplevel()
        Busqueda_ventana.title("Datos encontrados")

        # Crea variables vacías para guardar los datos de la fila
        Titulo = ""
        Descripcion = ""
        Prioridad = ""
        FechaLimite = ""
        TiempoEstimado = ""

        for row in result:
            Titulo = row[1]
            Descripcion = row[2]
            Prioridad = row[3]
            FechaLimite = row[4]
            TiempoEstimado = row[5]

        i = 1

        mensaje1 = tk.Message(Busqueda_ventana, text=Titulo, width=300, aspect=1000, font=("Arial", 14, "bold"), padx=10, pady=-2)
        mensaje1.grid(row=i*2+2, column=1)
        mensaje2 = tk.Message(Busqueda_ventana, text=Descripcion, width=200, aspect=1000, padx=60, pady=-2)
        mensaje2.grid(row=i*2+3, column=1)
        label = tk.Label(Busqueda_ventana, text="Prioridad:")
        label.grid(row=i*2+2, column=3)
        mensaje3 = tk.Message(Busqueda_ventana, text=Prioridad, width=200, aspect=1000)
        mensaje3.grid(row=i*2+3, column=3)
        label = tk.Label(Busqueda_ventana, text="Tiempo estimado:")
        label.grid(row=i*2+2, column=4)
        mensaje4 = tk.Message(Busqueda_ventana, text=FechaLimite, width=200, aspect=1000)
        mensaje4.grid(row=i*2+3, column=4)
        label = tk.Label(Busqueda_ventana, text="Fecha limite:")
        label.grid(row=i*2+2, column=5)
        mensaje5 = tk.Message(Busqueda_ventana, text=TiempoEstimado, width=200, aspect=1000)
        mensaje5.grid(row=i*2+3, column=5)

    else:
        messagebox.showinfo("Mensaje", "Dato no encontrado")

    cnx.commit()
        # Cierra la conexión
    cnx.close()

textboxsearch = tk.Text(master=Principal)
# Establece el ancho y alto del textbox en 10 caracteres
textboxsearch.config(width=60, height=1)
# Empaqueta el textbox en la ventana principal
textboxsearch.grid(row=0, column=1)

button = tk.Button(master=Principal, text="Buscar", command=buscar)
button.grid(row=0, column=2)

def actualizar():
    global Principal
    # Destruye la ventana principal
    Principal.destroy()
    # Crea la ventana principal de la aplicación
    Principal = tk.Tk()
    Principal.title("ToDoList")
    # Obtiene el ancho y alto de la pantalla
    screen_width = Principal.winfo_screenwidth()
    screen_height = Principal.winfo_screenheight()
    Principal.geometry(f"{screen_width}x{screen_height}")
    Principal.grid_columnconfigure(0, minsize=100)
    Principal.grid_rowconfigure(0, minsize=100)

    # Crea el botón y lo empaqueta
    button = tk.Button(text="Nueva Tarea", command=abrir_ventana)
    button.grid(row=0, column=0)


    """
    textbox_search = tk.Text(Principal)
    textbox_search.config(width=40, height=1)
    textbox_search.grid(row=0, column=1)
    """


    # Conectarse a la base de datos
    cnx = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="to_do_list"
        )
    cursor = cnx.cursor()

    # Recuperar los datos de la tabla (columna tarea y columna completado)
    query = "SELECT Titulo, Descripcion, Prioridad, FechaLimite, TiempoEstimado FROM tareas"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Iterar sobre cada fila y columna de los datos

    def completar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado):
        # Aquí puedes poner el código que quieras ejecutar al hacer clic en el botón
        print("Tarea completada:", titulo)

        cnx = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="to_do_list"
        )
        

        cursor = cnx.cursor()
        cursor.execute("DELETE FROM tareas WHERE Titulo = %s AND Descripcion = %s AND Prioridad = %s AND FechaLimite = %s AND TiempoEstimado = %s", (titulo, descripcion, prioridad, fechalimite, tiempoestimado))
        cnx.commit()

        today = date.today()

        sql = "SELECT * FROM registro_tareas WHERE fecha = %s"
        val = (today, )
        cursor.execute(sql, val)

        result = cursor.fetchall()

        if result:
            print("El dato existe en la tabla.")
            
            sql = "UPDATE registro_tareas SET tareas = tareas + 1 WHERE fecha = %s"
            val = (today, )
            cursor.execute(sql, val)

            print("si")
            cnx.commit()


        else:
            print("El dato no existe en la tabla.")

            sql = "INSERT INTO registro_tareas (fecha, tareas) VALUES (%s, 1)"
            val = (today, )
            cursor.execute(sql, val)
            cnx.commit()

        cnx.close()  # Cierra la conexión a la base de datos
        actualizar()

    def registro_tarea():

        today = date.today()

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="to_do_list"
        )

        mycursor = mydb.cursor()

        sql = "SELECT * FROM registro_tareas WHERE fecha = %s"
        val = (today, )
        mycursor.execute(sql, val)

        result = mycursor.fetchall()

        if result:
            print("El dato existe en la tabla.")
            
            sql = "UPDATE registro_tareas SET tareas = tareas + 1 WHERE fecha = %s"
            val = (today, )
            mycursor.execute(sql, val)

            print("si")
            mydb.commit()


        else:
            print("El dato no existe en la tabla.")

            sql = "INSERT INTO registro_tareas (fecha, tareas) VALUES (%s, 1)"
            val = (today, )
            mycursor.execute(sql, val)
            mydb.commit()

    def eliminar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado):
        # Aquí puedes poner el código que quieras ejecutar al hacer clic en el botón
        print("Tarea eliminada:", titulo)

        cnx = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="to_do_list"
        )
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM tareas WHERE Titulo = %s AND Descripcion = %s AND Prioridad = %s AND FechaLimite = %s AND TiempoEstimado = %s", (titulo, descripcion, prioridad, fechalimite, tiempoestimado))
        cnx.commit()
        cnx.close()  # Cierra la conexión a la base de datos
        actualizar()

    def editar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado):

        Editar_Tarea = tk.Tk()
        Editar_Tarea.title('Editar tarea')
        Editar_Tarea.geometry("325x600")
        Editar_Tarea.grid_columnconfigure(0, minsize=50)
        Editar_Tarea.grid_rowconfigure(0, minsize=50)


        label = tk.Label(Editar_Tarea, text="Escribe el titulo de la tarea:")
        label.grid(row=0, column=0)
        # Crea el textbox
        textboxtitle = tk.Text(Editar_Tarea)
        # Establece el ancho y alto del textbox en 10 caracteres
        textboxtitle.config(width=40, height=1)
        # Empaqueta el textbox en la ventana principal
        textboxtitle.grid(row=1, column=0)


        label = tk.Label(Editar_Tarea, text="Escribe la descripción de la tarea:")
        label.grid()
        # Crea el textbox
        textboxdes = tk.Text(Editar_Tarea)
        # Establece el ancho y alto del textbox en 10 caracteres
        textboxdes.config(width=40, height=5)
        # Empaqueta el textbox en la ventana principal
        textboxdes.grid()


        label = tk.Label(Editar_Tarea, text="Selecciona la prioridad de la tarea:")
        label.grid()
        # Crea una lista de opciones para el combobox
        options = ["Prioridad maxima", "Prioridad media", "Prioridad baja"]
        # Crea el combobox y lo empaqueta
        comboboxpriority = ttk.Combobox(Editar_Tarea, values=options)
        comboboxpriority.config(state="readonly")
        comboboxpriority.grid()



        label = tk.Label(Editar_Tarea, text="Selecciona el tiempo estimado para completar la tarea:")
        label.grid()
        # Crea una lista de opciones para el combobox
        options = ["10 minutos", "15 minutos", "30 minutos", "1 hora"]
        # Crea el combobox y lo empaqueta
        comboboxtime = ttk.Combobox(Editar_Tarea, values=options)
        comboboxtime.config(state="readonly")
        comboboxtime.grid()


        label = tk.Label(Editar_Tarea, text="Selecciona la fecha limite para completar la tarea:")
        label.grid()
        # Crea una lista de opciones para el combobox
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        # Crea el combobox y lo empaqueta
        comboboxdate1 = ttk.Combobox(Editar_Tarea, values=options)
        comboboxdate1.config(state="readonly")
        comboboxdate1.grid()

        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        # Crea el combobox y lo empaqueta
        comboboxdate2 = ttk.Combobox(Editar_Tarea, values=options)
        comboboxdate2.config(state="readonly")
        comboboxdate2.grid()

        options = ["2022", "2023", "2024", "2025"]
        # Crea el combobox y lo empaqueta
        comboboxdate3 = ttk.Combobox(Editar_Tarea, values=options)
        comboboxdate3.config(state="readonly")
        comboboxdate3.grid()


        def show_reminder():
            # Muestra el recordatorio en una ventana emergente
            messagebox.showinfo("Recordatorio", "¡No olvides hacer tu tarea:!")

        class ReminderThread(threading.Thread):
            def __init__(self, horas, minutos):
                self.horas = horas
                self.minutos = minutos
                super().__init__()

            def run(self):
                # Obtiene la hora actual
                current_time = time.localtime()
                # Calcula cuántos segundos faltan para que se cumpla la hora especificada
                seconds_left = (self.horas - current_time.tm_hour) * 3600 + (self.minutos - current_time.tm_min) * 60 - current_time.tm_sec
                # Detiene la ejecución del programa durante los segundos calculados
                time.sleep(seconds_left)
                # Muestra el recordatorio
                show_reminder()

        label = tk.Label(Editar_Tarea, text="Introduce la hora del recordatorio (0-23):")
        label.grid()
        # Crea una lista de opciones para el combobox
        options = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
        # Crea el combobox y lo empaqueta
        comboboxhoras = ttk.Combobox(Editar_Tarea, values=options)
        comboboxhoras.config(state="readonly")
        comboboxhoras.grid()

        label = tk.Label(Editar_Tarea, text="Introduce los minutos del recordatorio (0-59):")
        label.grid()
        # Crea una lista de opciones para el combobox
        options = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"
        ,"31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
        # Crea el combobox y lo empaqueta
        comboboxminutos = ttk.Combobox(Editar_Tarea, values=options)
        comboboxminutos.config(state="readonly")
        comboboxminutos.grid()    

        def actualizar_datos():

            print("si edita")
            
            titulo = textboxtitle.get("1.0", "end")
            descripcion = textboxdes.get("1.0", "end")
            prioridad = comboboxpriority.get()
            tiempoestimado = comboboxtime.get()
            fechalimite1 = comboboxdate1.get()
            fechalimite2 = comboboxdate2.get()
            fechalimite3 = comboboxdate3.get()
            fechalimite = fechalimite1+"/"+fechalimite2+"/"+fechalimite3
            horas = int(comboboxhoras.get())
            minutos = int(comboboxminutos.get())
            horas = horas
            minutos = minutos


            cnx = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="to_do_list"
            )
            cursor = cnx.cursor()

            id_tarea = None

            cursor.execute("SELECT id FROM to_do_list.tareas WHERE Titulo = %s AND Descripcion = %s", (titulo, descripcion))
            result = cursor.fetchone()
            if result:
                id_tarea = result[0]
                print("idtarea1: " + id_tarea)

            print("idtarea2: " + id_tarea)

            cursor.execute("UPDATE to_do_list.tareas SET Prioridad = %s, FechaLimite = %s, TiempoEstimado = %s WHERE id = %s", (prioridad, fechalimite, tiempoestimado, id_tarea))
            cnx.commit()

            # Cierra la conexión
            cnx.close()

            thread = ReminderThread(horas, minutos)
            thread.start()

            """
            if horas or minutos == "":
                print("no recordatorio")
            else:
                #Crea una instancia de ReminderThread y la ejecuta en un hilo en segundo plano
                thread = ReminderThread(horas, minutos)
                thread.start()
            """

            Editar_Tarea.destroy()
            actualizar()

        button = tk.Button(Editar_Tarea, text="Editar tarea", command = actualizar_datos)
        button.grid()


        

    figure = Figure(figsize=(7, 4), dpi=100)
    canvas = FigureCanvasTkAgg(figure, master=Principal)
    canvas.get_tk_widget().grid(row=0, column=0)

    ax = figure.add_subplot(111)



    sql = "SELECT fecha, SUM(tareas) as tareas FROM registro_tareas WHERE fecha >= DATE_SUB(NOW(), INTERVAL 5 DAY) GROUP BY fecha ORDER BY fecha DESC"
    cursor.execute(sql)
    result = cursor.fetchall()

    fechas = []
    tareas = []
    for row in result:
        #fecha = row[0]
        #fecha_formateada = fecha.strftime("%d/%m/%Y")
        #fechas.append(fecha_formateada)
        fechas.append(row[0])
        tareas.append(row[1])

    ax.bar(fechas, tareas)

    ax.set_xlabel('Fechas')
    ax.set_ylabel('Tareas completadas')
    ax.set_ylim(0, 15)
    ax.set_title('Histograma de tareas completadas por día')
    canvas.get_tk_widget().grid(row=1, column=7)

    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            # Asigna cada valor de cada columna a una variable diferente
            Titulo = row[0]
            Descripcion = row[1]
            Prioridad = row[2]
            FechaLimite = row[3]
            TiempoEstimado = row[4]

            mensaje1 = tk.Message(Principal, text=Titulo, width=300, aspect=1000, font=("Arial", 14, "bold"), padx=10, pady=-2)
            mensaje1.grid(row=i*2+2, column=1)
            mensaje2 = tk.Message(Principal, text=Descripcion, width=200, aspect=1000, padx=60, pady=-2)
            mensaje2.grid(row=i*2+3, column=1)
            label = tk.Label(Principal, text="Prioridad:")
            label.grid(row=i*2+2, column=3)
            mensaje3 = tk.Message(Principal, text=Prioridad, width=200, aspect=1000)
            mensaje3.grid(row=i*2+3, column=3)
            label = tk.Label(Principal, text="Tiempo estimado:")
            label.grid(row=i*2+2, column=4)
            mensaje4 = tk.Message(Principal, text=FechaLimite, width=200, aspect=1000)
            mensaje4.grid(row=i*2+3, column=4)
            label = tk.Label(Principal, text="Fecha limite:")
            label.grid(row=i*2+2, column=5)
            mensaje5 = tk.Message(Principal, text=TiempoEstimado, width=200, aspect=1000)
            mensaje5.grid(row=i*2+3, column=5)

            if j % 5 == 0:
                completar = tk.Button(Principal, text="Completar", command=lambda titulo=Titulo, descripcion=Descripcion, prioridad=Prioridad , fechalimite=FechaLimite, tiempoestimado=TiempoEstimado  : completar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado))
                completar.grid(row=i*2+2, column=j)
                editar = tk.Button(Principal, text="Editar", command=lambda titulo=Titulo, descripcion=Descripcion, prioridad=Prioridad , fechalimite=FechaLimite, tiempoestimado=TiempoEstimado  : editar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado))
                editar.grid(row=i*2+2, column=6)
                eliminar = tk.Button(Principal, text="Eliminar", command=lambda titulo=Titulo, descripcion=Descripcion, prioridad=Prioridad , fechalimite=FechaLimite, tiempoestimado=TiempoEstimado  : eliminar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado))
                eliminar.grid(row=i*2+3, column=6)
                break
    cnx.commit()
    cnx.close()


    # Inicia el bucle de eventos de Tkinter
    Principal.mainloop()




# Crea el botón y lo empaqueta
button = tk.Button(text="Nueva Tarea", command=abrir_ventana)
button.grid(row=0, column=0)


"""
textbox_search = tk.Text(Principal)
textbox_search.config(width=40, height=1)
textbox_search.grid(row=0, column=1)
"""


# Conectarse a la base de datos
cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="to_do_list"
    )
cursor = cnx.cursor()

# Recuperar los datos de la tabla (columna tarea y columna completado)
query = "SELECT Titulo, Descripcion, Prioridad, FechaLimite, TiempoEstimado FROM tareas"
cursor.execute(query)
rows = cursor.fetchall()

# Iterar sobre cada fila y columna de los datos

def completar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado):
    # Aquí puedes poner el código que quieras ejecutar al hacer clic en el botón
    print("Tarea completada:", titulo)

    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="to_do_list"
    )
    

    cursor = cnx.cursor()
    cursor.execute("DELETE FROM tareas WHERE Titulo = %s AND Descripcion = %s AND Prioridad = %s AND FechaLimite = %s AND TiempoEstimado = %s", (titulo, descripcion, prioridad, fechalimite, tiempoestimado))
    cnx.commit()

    today = date.today()

    sql = "SELECT * FROM registro_tareas WHERE fecha = %s"
    val = (today, )
    cursor.execute(sql, val)

    result = cursor.fetchall()

    if result:
        print("El dato existe en la tabla.")
        
        sql = "UPDATE registro_tareas SET tareas = tareas + 1 WHERE fecha = %s"
        val = (today, )
        cursor.execute(sql, val)

        print("si")
        cnx.commit()


    else:
        print("El dato no existe en la tabla.")

        sql = "INSERT INTO registro_tareas (fecha, tareas) VALUES (%s, 1)"
        val = (today, )
        cursor.execute(sql, val)
        cnx.commit()

    cnx.close()  # Cierra la conexión a la base de datos
    actualizar()

def registro_tarea():

    today = date.today()

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="to_do_list"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM registro_tareas WHERE fecha = %s"
    val = (today, )
    mycursor.execute(sql, val)

    result = mycursor.fetchall()

    if result:
        print("El dato existe en la tabla.")
        
        sql = "UPDATE registro_tareas SET tareas = tareas + 1 WHERE fecha = %s"
        val = (today, )
        mycursor.execute(sql, val)

        print("si")
        mydb.commit()


    else:
        print("El dato no existe en la tabla.")

        sql = "INSERT INTO registro_tareas (fecha, tareas) VALUES (%s, 1)"
        val = (today, )
        mycursor.execute(sql, val)
        mydb.commit()

def eliminar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado):
    # Aquí puedes poner el código que quieras ejecutar al hacer clic en el botón
    print("Tarea eliminada:", titulo)

    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="to_do_list"
    )
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM tareas WHERE Titulo = %s AND Descripcion = %s AND Prioridad = %s AND FechaLimite = %s AND TiempoEstimado = %s", (titulo, descripcion, prioridad, fechalimite, tiempoestimado))
    cnx.commit()
    cnx.close()  # Cierra la conexión a la base de datos
    actualizar()

def editar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado):

    Editar_Tarea = tk.Tk()
    Editar_Tarea.title('Editar tarea')
    Editar_Tarea.geometry("325x600")
    Editar_Tarea.grid_columnconfigure(0, minsize=50)
    Editar_Tarea.grid_rowconfigure(0, minsize=50)


    label = tk.Label(Editar_Tarea, text="Escribe el titulo de la tarea:")
    label.grid(row=0, column=0)
    # Crea el textbox
    textboxtitle = tk.Text(Editar_Tarea)
    # Establece el ancho y alto del textbox en 10 caracteres
    textboxtitle.config(width=40, height=1)
    # Empaqueta el textbox en la ventana principal
    textboxtitle.grid(row=1, column=0)


    label = tk.Label(Editar_Tarea, text="Escribe la descripción de la tarea:")
    label.grid()
    # Crea el textbox
    textboxdes = tk.Text(Editar_Tarea)
    # Establece el ancho y alto del textbox en 10 caracteres
    textboxdes.config(width=40, height=5)
    # Empaqueta el textbox en la ventana principal
    textboxdes.grid()


    label = tk.Label(Editar_Tarea, text="Selecciona la prioridad de la tarea:")
    label.grid()
    # Crea una lista de opciones para el combobox
    options = ["Prioridad maxima", "Prioridad media", "Prioridad baja"]
    # Crea el combobox y lo empaqueta
    comboboxpriority = ttk.Combobox(Editar_Tarea, values=options)
    comboboxpriority.config(state="readonly")
    comboboxpriority.grid()



    label = tk.Label(Editar_Tarea, text="Selecciona el tiempo estimado para completar la tarea:")
    label.grid()
    # Crea una lista de opciones para el combobox
    options = ["10 minutos", "15 minutos", "30 minutos", "1 hora"]
    # Crea el combobox y lo empaqueta
    comboboxtime = ttk.Combobox(Editar_Tarea, values=options)
    comboboxtime.config(state="readonly")
    comboboxtime.grid()


    label = tk.Label(Editar_Tarea, text="Selecciona la fecha limite para completar la tarea:")
    label.grid()
    # Crea una lista de opciones para el combobox
    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    # Crea el combobox y lo empaqueta
    comboboxdate1 = ttk.Combobox(Editar_Tarea, values=options)
    comboboxdate1.config(state="readonly")
    comboboxdate1.grid()

    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    # Crea el combobox y lo empaqueta
    comboboxdate2 = ttk.Combobox(Editar_Tarea, values=options)
    comboboxdate2.config(state="readonly")
    comboboxdate2.grid()

    options = ["2022", "2023", "2024", "2025"]
    # Crea el combobox y lo empaqueta
    comboboxdate3 = ttk.Combobox(Editar_Tarea, values=options)
    comboboxdate3.config(state="readonly")
    comboboxdate3.grid()


    def show_reminder():
        # Muestra el recordatorio en una ventana emergente
        messagebox.showinfo("Recordatorio", "¡No olvides hacer tu tarea:!")

    class ReminderThread(threading.Thread):
        def __init__(self, horas, minutos):
            self.horas = horas
            self.minutos = minutos
            super().__init__()

        def run(self):
            # Obtiene la hora actual
            current_time = time.localtime()
            # Calcula cuántos segundos faltan para que se cumpla la hora especificada
            seconds_left = (self.horas - current_time.tm_hour) * 3600 + (self.minutos - current_time.tm_min) * 60 - current_time.tm_sec
            # Detiene la ejecución del programa durante los segundos calculados
            time.sleep(seconds_left)
            # Muestra el recordatorio
            show_reminder()

    label = tk.Label(Editar_Tarea, text="Introduce la hora del recordatorio (0-23):")
    label.grid()
    # Crea una lista de opciones para el combobox
    options = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
    # Crea el combobox y lo empaqueta
    comboboxhoras = ttk.Combobox(Editar_Tarea, values=options)
    comboboxhoras.config(state="readonly")
    comboboxhoras.grid()

    label = tk.Label(Editar_Tarea, text="Introduce los minutos del recordatorio (0-59):")
    label.grid()
    # Crea una lista de opciones para el combobox
    options = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"
    ,"31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
    # Crea el combobox y lo empaqueta
    comboboxminutos = ttk.Combobox(Editar_Tarea, values=options)
    comboboxminutos.config(state="readonly")
    comboboxminutos.grid()    

    def actualizar_datos():

        print("si edita")
        
        titulo = textboxtitle.get("1.0", "end")
        descripcion = textboxdes.get("1.0", "end")
        prioridad = comboboxpriority.get()
        tiempoestimado = comboboxtime.get()
        fechalimite1 = comboboxdate1.get()
        fechalimite2 = comboboxdate2.get()
        fechalimite3 = comboboxdate3.get()
        fechalimite = fechalimite1+"/"+fechalimite2+"/"+fechalimite3
        horas = int(comboboxhoras.get())
        minutos = int(comboboxminutos.get())
        horas = horas
        minutos = minutos



        cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="to_do_list"
        )
        cursor = cnx.cursor()
        cursor.execute("SELECT id FROM tareas WHERE Titulo = %s AND Descripcion = %s AND Prioridad = %s AND FechaLimite = %s AND TiempoEstimado = %s", (titulo, descripcion, prioridad, fechalimite, tiempoestimado))
        result = cursor.fetchone()
        if result:
            id = result[0]
            print("id:", id)
        else:
            print("No se encontraron registros con esos parametros")


        cursor.execute("UPDATE to_do_list.tareas SET Titulo = %s, Descripcion = %s, Prioridad = %s, FechaLimite = %s, TiempoEstimado = %s WHERE id = %s", (titulo, descripcion, prioridad, tiempoestimado, fechalimite, 16))
        cnx.commit()

        # Cierra la conexión
        cnx.close()

        thread = ReminderThread(horas, minutos)
        thread.start()

        """
        if horas or minutos == "":
            print("no recordatorio")
        else:
             #Crea una instancia de ReminderThread y la ejecuta en un hilo en segundo plano
            thread = ReminderThread(horas, minutos)
            thread.start()
        """

        Editar_Tarea.destroy()
        actualizar()

    button = tk.Button(Editar_Tarea, text="Editar tarea", command = actualizar_datos)
    button.grid()


    

figure = Figure(figsize=(7, 4), dpi=100)
canvas = FigureCanvasTkAgg(figure, master=Principal)
canvas.get_tk_widget().grid(row=0, column=0)

ax = figure.add_subplot(111)



sql = "SELECT fecha, SUM(tareas) as tareas FROM registro_tareas WHERE fecha >= DATE_SUB(NOW(), INTERVAL 5 DAY) GROUP BY fecha ORDER BY fecha DESC"
cursor.execute(sql)
result = cursor.fetchall()

fechas = []
tareas = []
for row in result:
    #fecha = row[0]
    #fecha_formateada = fecha.strftime("%d/%m/%Y")
    #fechas.append(fecha_formateada)
    fechas.append(row[0])
    tareas.append(row[1])

ax.bar(fechas, tareas)

ax.set_xlabel('Fechas')
ax.set_ylabel('Tareas completadas')
ax.set_ylim(0, 15)
ax.set_title('Histograma de tareas completadas por día')
canvas.get_tk_widget().grid(row=1, column=7)

for i, row in enumerate(rows):
    for j, col in enumerate(row):
        # Asigna cada valor de cada columna a una variable diferente
        Titulo = row[0]
        Descripcion = row[1]
        Prioridad = row[2]
        FechaLimite = row[3]
        TiempoEstimado = row[4]

        mensaje1 = tk.Message(Principal, text=Titulo, width=300, aspect=1000, font=("Arial", 14, "bold"), padx=10, pady=-2)
        mensaje1.grid(row=i*2+2, column=1)
        mensaje2 = tk.Message(Principal, text=Descripcion, width=200, aspect=1000, padx=60, pady=-2)
        mensaje2.grid(row=i*2+3, column=1)
        label = tk.Label(Principal, text="Prioridad:")
        label.grid(row=i*2+2, column=3)
        mensaje3 = tk.Message(Principal, text=Prioridad, width=200, aspect=1000)
        mensaje3.grid(row=i*2+3, column=3)
        label = tk.Label(Principal, text="Tiempo estimado:")
        label.grid(row=i*2+2, column=4)
        mensaje4 = tk.Message(Principal, text=FechaLimite, width=200, aspect=1000)
        mensaje4.grid(row=i*2+3, column=4)
        label = tk.Label(Principal, text="Fecha limite:")
        label.grid(row=i*2+2, column=5)
        mensaje5 = tk.Message(Principal, text=TiempoEstimado, width=200, aspect=1000)
        mensaje5.grid(row=i*2+3, column=5)

        if j % 5 == 0:
            completar = tk.Button(Principal, text="Completar", command=lambda titulo=Titulo, descripcion=Descripcion, prioridad=Prioridad , fechalimite=FechaLimite, tiempoestimado=TiempoEstimado  : completar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado))
            completar.grid(row=i*2+2, column=j)
            editar = tk.Button(Principal, text="Editar", command=lambda titulo=Titulo, descripcion=Descripcion, prioridad=Prioridad , fechalimite=FechaLimite, tiempoestimado=TiempoEstimado  : editar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado))
            editar.grid(row=i*2+2, column=6)
            eliminar = tk.Button(Principal, text="Eliminar", command=lambda titulo=Titulo, descripcion=Descripcion, prioridad=Prioridad , fechalimite=FechaLimite, tiempoestimado=TiempoEstimado  : eliminar_tarea(titulo, descripcion, prioridad, fechalimite, tiempoestimado))
            eliminar.grid(row=i*2+3, column=6)
            break
cnx.commit()
cnx.close()


# Inicia el bucle de eventos de Tkinter
Principal.mainloop()