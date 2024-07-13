import datetime
import platform
import shutil
import traceback
from PySide6.QtWidgets import *
from PySide6 import QtCore
from PySide6.QtCore import *
import psutil
from qt_material import *
from ui_si import *
from time import sleep
import sys

platforms = {
    'linux' : 'Linux',
    'linux1' : 'Linux',
    'linux2' : 'Linux',
    'darvin' : 'OS X',
    'win32' : 'Windows'
}

class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        
        self.kwargs['progress_callback'] = self.signals.progress
        
    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
            
        finally:
            self.signals.finished.emit()
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        
        self.setupUi(self)
        self.app = app
        
        apply_stylesheet(self.app, theme = 'dark_cyan.xml')
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.centralWidget().setGraphicsEffect(self.shadow)
        
        self.setWindowTitle("System Information")
        
        QSizeGrip(self.size_grip)
        
        self.min_win_btn.clicked.connect(lambda: self.showMinimized())
        self.close_win_btn.clicked.connect(lambda: self.close())
        self.restore_win_btn.clicked.connect(lambda: self.restore_or_maximize_window())
        
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.cpu_and_memory))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.battery))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.system_information))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.activities))
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.storage))
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.sensors))
        self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.networks))
        
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        
        self.header_frame.mouseMoveEvent = moveWindow
        
        self.pushButton.clicked.connect(lambda: self.sildeLeftMenu())
        
        
        for w in self.menu_frame.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)
        
        self.threadpool = QThreadPool()
        
        self.show()
        #self.battery_info()
        #self.cpu_ram_info()
        self.system_info()
        self.activity_info()
        self.storage_info()
        self.sensor_info()
        self.network_info()
        self.psutil_thread()
        
    def print_output(self, s):
        print(s)
        
    def thread_complete(self):
        print("thread complete!")
        
    def progress_fn(self, n):
        print("%d%% done" % n)
        
    def psutil_thread(self):
        worker = Worker(self.cpu_ram_info)
        
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(worker)
        
        battery_worker = Worker(self.battery_info)
        battery_worker.signals.result.connect(self.print_output)
        battery_worker.signals.finished.connect(self.thread_complete)
        battery_worker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(battery_worker)
        
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def sildeLeftMenu(self):
        width = self.left_menu_cont_frame.width()
        if width == 40:
            newWidth = 200
        else:
            newWidth = 40
            
        self.animation = QtCore.QPropertyAnimation(self.left_menu_cont_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        
    def applyButtonStyle(self):
        for w in self.menu_frame.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName():
                w.setStyleSheet("border-bottom: none;")
                
        self.sender().setStyleSheet("border-bottom: 2px solid")
        return
    
    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)
    
    def battery_info(self, progress_callback):
        while True:
            if not hasattr (psutil, "sensors_battery"):
                self.batt_status.setText("Platform not supported")
                print("work here for platform")
                return
            
            batt = psutil.sensors_battery()
            if batt is None:
                self.batt_status.setText("No battery installed")
                print("work here for install battery")
                return
                
            if batt.power_plugged:
                self.charge_status.setText(str(round(batt.percent, 2))+"%")
                self.batt_time.setText("N/A")
                
                if batt.percent < 100:
                    self.batt_status.setText("Charging")
                else:
                    self.batt_status.setText("Fully charged")

                self.plug_status.setText("Yes")
            else:
                self.charge_status.setText(str(round(batt.percent, 2))+"%")
                self.batt_time.setText(self.secs2hours(batt.secsleft))
                if batt.percent < 100:
                    self.batt_status.setText("Discharging")
                else:
                    self.batt_status.setText("Fully charged")
                
                self.plug_status.setText("No")
                
                sleep(1)
                
    def cpu_ram_info(self, progress_callback):
        while True:
            totalRam = 1.0
            totalRam = psutil.virtual_memory()[0] * totalRam
            totalRam /= (1024**3)
            self.total_ram.setText(str("{:.4f}".format(totalRam)+ 'GB'))
            
            availRam = 1.0
            availRam = psutil.virtual_memory()[1] * availRam
            availRam /= (1024**3)
            self.avai_ram.setText(str("{:.4f}".format(availRam)+ 'GB'))
            
            ramUsage = str(psutil.virtual_memory()[2]) + '%'
            self.ram_usage.setText(str(format(ramUsage)+ ' GB'))
            
            ramUsed = 1.0
            ramUsed = psutil.virtual_memory()[3] * ramUsed
            ramUsed /= (1024**3)
            self.used_ram.setText(str("{:.4f}".format(ramUsed)+ 'GB'))
            
            ramFree = 1.0
            ramFree = psutil.virtual_memory()[4] * ramFree
            ramFree /= (1024**3)
            self.free_ram.setText(str("{:.4f}".format(ramFree)+ 'GB'))
            
            
            cores = psutil.cpu_count()
            self.cpu_count.setText(str(cores))
            
            cpuPer = psutil.cpu_percent()
            self.cpu_per.setText(str(cpuPer)+ " %")
            
            mainCore = psutil.cpu_count(logical = False)
            self.main_core.setText(str(mainCore))
            
            sleep(1)
            
    def system_info(self):
        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.system_time.setText(time)
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.system_date.setText(date)
        
        self.system_os.setText(platform.system())
        self.system_machine.setText(platform.machine())
        self.system_platform.setText(platform.platform()+" ")
        self.system_version.setText(platform.version())
        self.system_processor.setText(platform.processor())
        
    def crete_table_widget(self, rowPosition, colPosition, text, tableName):
        qtwi = QTableWidgetItem()
        getattr(self, tableName).setItem(rowPosition, colPosition, qtwi)
        qtwi = getattr(self, tableName).item(rowPosition, colPosition)
        qtwi.setText(text)   
    
    def activity_info(self):
        for p in psutil.pids():
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            try:
                activity = psutil.Process(p)
                self.crete_table_widget(rowPosition, 0, str(activity.pid), "tableWidget")
                self.crete_table_widget(rowPosition, 1, activity.name(), "tableWidget")
                self.crete_table_widget(rowPosition, 2, activity.status(), "tableWidget")
                self.crete_table_widget(rowPosition, 3, str(datetime.datetime.utcfromtimestamp(activity.create_time()).strftime('%Y-%m-%d %H:%M:%S')), "tableWidget")
                
                suspend_btn = QPushButton(self.tableWidget)
                suspend_btn.setText('Suspend')
                suspend_btn.setStyleSheet("color: brown")
                self.tableWidget.setCellWidget(rowPosition, 4, suspend_btn)
                
                resume_btn = QPushButton(self.tableWidget)
                resume_btn.setText('Resume')
                resume_btn.setStyleSheet("color: green")
                self.tableWidget.setCellWidget(rowPosition, 5, resume_btn)
                
                terminate_btn = QPushButton(self.tableWidget)
                terminate_btn.setText("Terminate")
                terminate_btn.setStyleSheet("color: orange")
                self.tableWidget.setCellWidget(rowPosition, 6, terminate_btn)
                
                kill_btn = QPushButton(self.tableWidget)
                kill_btn.setText("Kill")
                kill_btn.setStyleSheet("color: red")
                self.tableWidget.setCellWidget(rowPosition, 7, kill_btn)
                
            except Exception as e:
                print(e)
                
        self.search_activity_lineEdit.textChanged.connect(self.findName)
        
    def findName(self):
        name = self.search_activity_lineEdit.text().lower()
        
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 1)
            self.tableWidget.setRowHidden(row, name not in item.text().lower())
            
    def storage_info(self):
        global platforms
        storage_devices = psutil.disk_partitions(all = False)
        z = 0
        for x in storage_devices:
            rowPosition = self.storage_table.rowCount()
            self.storage_table.insertRow(rowPosition)
            
            self.crete_table_widget(rowPosition, 0, x.device, "storage_table")
            self.crete_table_widget(rowPosition, 1, x.mountpoint, "storage_table")
            self.crete_table_widget(rowPosition, 2, x.fstype, "storage_table")
            self.crete_table_widget(rowPosition, 3, x.opts, "storage_table")
            
            if sys.platform == 'linux'  or sys.platform == 'linux1' or sys.platform == 'linux2':
                self.crete_table_widget(rowPosition, 4, str(x.maxfile), "storage_table")
                self.crete_table_widget(rowPosition, 5, x.maxpath, "storage_table")
            else:
                self.crete_table_widget(rowPosition, 4, "function not available on " + platforms[sys.platform], "storage_table")
                self.crete_table_widget(rowPosition, 5, "function not available on " + platforms[sys.platform], "storage_table")
            
            disk_usage = shutil.disk_usage(x.mountpoint)
            self.crete_table_widget(rowPosition, 6, str((disk_usage.total / (1024**3))) + " GB", "storage_table")
            self.crete_table_widget(rowPosition, 7, str((disk_usage.free / (1024**3))) + " GB", "storage_table")
            self.crete_table_widget(rowPosition, 8, str((disk_usage.used / (1024**3))) + " GB", "storage_table")
            
            full_disk = (disk_usage.used / disk_usage.total) * 100
            prog_bar = QProgressBar(self.storage_table)
            prog_bar.setObjectName(u"prog_bar")
            prog_bar.setValue(full_disk)
            self.storage_table.setCellWidget(rowPosition, 9, prog_bar)
            
    def sensor_info(self):        
        if sys.platform == 'linux'  or sys.platform == 'linux1' or sys.platform == 'linux2':
                
            for s in psutil.sensors_temeratures():
                for i in psutil.sensors_temeratures()[s]:
                    rowPosition = self.sensor_table.rowCount()
                    self.sensor_table.insertRow(rowPosition)
                        
                    self.crete_table_widget(rowPosition, 0, s, "sensor_table")
                    self.crete_table_widget(rowPosition, 1, i.label, "sensor_table")
                    self.crete_table_widget(rowPosition, 2, str(i.current), "sensor_table")
                    self.crete_table_widget(rowPosition, 3, str(i.high), "sensor_table")
                    self.crete_table_widget(rowPosition, 4, str(i.critical), "sensor_table")
                    
                    temp_per = (i.current / i .high) * 100
                    prog_bar = QProgressBar(self.sensor_table)
                    prog_bar.setObjectName(u"prog_bar")
                    prog_bar.setValue(temp_per)
                    self.sensor_table.setCellWidget(rowPosition, 5, prog_bar)
        else:
            global platforms
            rowPosition = self.sensor_table.rowCount()
            self.sensor_table.insertRow(rowPosition)
            
            self.crete_table_widget(rowPosition, 0, "function not available on " + platforms[sys.platform], "sensor_table")
            
            self.crete_table_widget(rowPosition, 1, "N/A", "sensor_table")
            self.crete_table_widget(rowPosition, 2, "N/A", "sensor_table")
            self.crete_table_widget(rowPosition, 3, "N/A", "sensor_table")
            self.crete_table_widget(rowPosition, 4, "N/A", "sensor_table")
            self.crete_table_widget(rowPosition, 5, "N/A", "sensor_table")
            
    def network_info(self):
        for n in psutil.net_if_stats():
            z = psutil.net_if_stats()
            
            rowPosition = self.net_stats_table.rowCount()
            self.net_stats_table.insertRow(rowPosition)
            
            self.crete_table_widget(rowPosition, 0, n, "net_stats_table")
            self.crete_table_widget(rowPosition, 1, str(z[n].isup), "net_stats_table")
            self.crete_table_widget(rowPosition, 2, str(z[n].duplex), "net_stats_table")
            self.crete_table_widget(rowPosition, 3, str(z[n].speed), "net_stats_table")
            self.crete_table_widget(rowPosition, 4, str(z[n].mtu), "net_stats_table")
            
        for c in psutil.net_io_counters(pernic = True):
            z = psutil.net_io_counters(pernic = True)
            
            rowPosition = self.net_io_table.rowCount()
            self.net_io_table.insertRow(rowPosition)
            
            self.crete_table_widget(rowPosition, 0, c, "net_io_table")
            self.crete_table_widget(rowPosition, 1, str(z[c].bytes_sent), "net_io_table")
            self.crete_table_widget(rowPosition, 2, str(z[c].bytes_recv), "net_io_table")
            self.crete_table_widget(rowPosition, 3, str(z[c].packets_sent), "net_io_table")
            self.crete_table_widget(rowPosition, 4, str(z[c].packets_recv), "net_io_table")
            self.crete_table_widget(rowPosition, 5, str(z[c].errin), "net_io_table")
            self.crete_table_widget(rowPosition, 6, str(z[c].errout), "net_io_table")
            self.crete_table_widget(rowPosition, 7, str(z[c].dropin), "net_io_table")
            self.crete_table_widget(rowPosition, 8, str(z[c].dropout), "net_io_table")
        
        for a in psutil.net_if_addrs():
            z = psutil.net_if_addrs()
            
            for i in z[a]:
                rowPosition = self.net_address_table.rowCount()
                self.net_address_table.insertRow(rowPosition)
                self.crete_table_widget(rowPosition, 0, str(a), "net_address_table")
                self.crete_table_widget(rowPosition, 1, str(i.family), "net_address_table")
                self.crete_table_widget(rowPosition, 2, str(i.address), "net_address_table")
                self.crete_table_widget(rowPosition, 3, str(i.netmask), "net_address_table")
                self.crete_table_widget(rowPosition, 4, str(i.broadcast), "net_address_table")
                self.crete_table_widget(rowPosition, 5, str(i.ptp), "net_address_table")
                
                
        for c in psutil.net_connections():
            z = psutil.net_connections()
            rowPosition = self.net_connec_table.rowCount()
            self.net_connec_table.insertRow(rowPosition)
            
            self.crete_table_widget(rowPosition, 0, str(c.fd), "net_connec_table")
            self.crete_table_widget(rowPosition, 1, str(c.family), "net_connec_table")
            self.crete_table_widget(rowPosition, 2, str(c.type), "net_connec_table")
            self.crete_table_widget(rowPosition, 3, str(c.laddr), "net_connec_table")
            self.crete_table_widget(rowPosition, 4, str(c.raddr), "net_connec_table")
            self.crete_table_widget(rowPosition, 5, str(c.status), "net_connec_table")
            self.crete_table_widget(rowPosition, 6, str(c.pid), "net_connec_table")