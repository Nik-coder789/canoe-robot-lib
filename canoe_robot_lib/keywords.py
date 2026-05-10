from robot.api.deco import keyword
from robot.api import logger
from robot.api import Failure
from py_canoe import CANoe
import cantools
import os,cv2,time
import numpy as np
from datetime import datetime
import win32com.client
class CanoeLibrary:

    def __init__(self):
        self.canoe = CANoe()

    @keyword("Start CANoe")
    def start_canoe(self, cfg_path):
        if not cfg_path:
            raise Exception("Config path is required")
        print(f"[INFO] Opening CANoe config: {cfg_path}")
        self.canoe.open(cfg_path)
        self.canoe.start_measurement()
        print("[INFO] CANoe measurement started")

    @keyword("Stop CANoe")
    def stop_canoe(self):
        print("[INFO] Stopping CANoe measurement")
        self.canoe.stop_measurement()

    @keyword("Get Signal")
    def get_signal(self, bus, channel, message, signal):
        if not all([bus, channel, message, signal]):
            raise Exception("All parameters (bus, channel, message, signal) are required")

        value = self.canoe.get_signal_value(bus, channel, message, signal)

        print(f"[INFO] Signal Read -> Bus:{bus}, Channel:{channel}, Msg:{message}, Signal:{signal}, Value:{value}")

        return value
    @keyword("Set Signal")
    def set_signal(self, bus, channel, message, signal,value):
        if not all([bus, channel, message, signal, value]):
            raise Exception("All parameters (bus, channel, message, signal, value) are required")
        self.canoe.set_signal_value(bus, channel, message, signal, value)
        print(f"[INFO] Signal Write -> Bus:{bus}, Channel:{channel}, Msg:{message}, Signal:{signal}, Value:{value}")
    
    @keyword("Send diagReq")
    def send_diagreq(self,Ecu_qualifier_name,Request):
        if not all([Ecu_qualifier_name,Request]):
            raise Exception("Both parameters (Ecu_qualifier_name,Request) are required in str format")
        resp=self.canoe.send_diag_request(Ecu_qualifier_name,Request,True)
        self.last_resp=resp
        print(f"[INFO] Request sent --> {Request}")

    @keyword("Set Environment_Variable")
    def set_envar(self,env_var_name,value):
        if not all([env_var_name,value]):
            raise Exception("Both parameters (env_var_name,value) are required")
        self.canoe.set_environment_variable_value(env_var_name,value)
        print(f"[INFO] Environment_Var Write --> {env_var_name}={value}")
    
    @keyword("Get Environment_Variable")
    def get_envar(self,env_var_name):
        if not all([env_var_name]):
            raise Exception("env_var_name is required")
        value=self.canoe.get_environment_variable_value(env_var_name)
        print(f"[INFO] Environment_Var Read --> {env_var_name}={value}")
        return value
    
    @keyword("Set SysVar_Value")
    def set_sysvar(self,sys_var_name,value):
        if not all([sys_var_name,value]):
            raise Exception("Both parameters (sys_var_name,value) are required")
        self.canoe.set_system_variable_value(sys_var_name,value)
        print(f"[INFO] System_Var Write --> {sys_var_name}={value}")
    
    @keyword("Get SysVar_Value")
    def get_sysvar(self,sys_var_name):
        if not all([sys_var_name]):
            raise Exception("sys_var_name is required")
        value=self.canoe.get_system_variable_value(sys_var_name)
        print(f"[INFO] System_Var Read --> {sys_var_name}={value}")
        return(value)
    
    @keyword("Set Replay_block")
    def set_block(self,block_name, recording_file_path):
        if not all([block_name, recording_file_path]):
            raise Exception("Both parameters (block_name, recording_file_path) are required")
        self.canoe.set_replay_block_file(block_name,recording_file_path)
        print(f"[INFO] Set Replay block --> {block_name}={recording_file_path}")

    @keyword("Run Replay_block")
    def run_rply(self,block_name,strt_stp:bool):
        if block_name is None or strt_stp is None:
            raise Exception("Both parameters required")
        self.canoe.control_replay_block(block_name, strt_stp)
        print(f"[INFO] Replay block {'Started' if strt_stp else 'Stopped'} --> {block_name}")
    
    @keyword("Execute Test_Module")
    def test_module(self,test_module_name):
        if not all([test_module_name]):
            raise Exception("test_module_name is required")
        self.canoe.execute_test_module(test_module_name)
        print(f"[INFO] Executing test module --> {test_module_name}")
    
    @keyword("Execute Test Environement")
    def test_env(self,test_environment_name):
        if not all([test_environment_name]):
            raise Exception("test_environment_name is required")
        self.canoe.execute_all_test_modules_in_test_env(test_environment_name)
        print(f"[INFO] Executing Test Environment --> {test_environment_name}")
        
    @keyword("Execute all Test_env")
    def test_allenv(self):
        self.canoe.execute_all_test_environments()
        print("[INFO] Executing all Test Environments")
    
    @keyword("Write")
    def write_txt(self,text:str):
        self.canoe.write_text_in_write_window(text)
    
    @keyword("Validate Signal value")
    def validate(self,bus, channel, message, signal,expected_value):
        if bus is None or channel is None or message is None or signal is None or expected_value is None:
            raise Exception("All parameters (bus, channel, message, signal, expected_value) are required")
        val=self.canoe.get_signal_value(bus,channel,message,signal)
        if float(val)!=float(expected_value):
            raise Exception(f"Signal {signal} expected {expected_value} but got {val}")
        print(f"[PASS] {signal} == {expected_value}")
    
    @keyword("Get diagresp")
    def check_rsp(self):
        if not hasattr(self, "last_resp"):
            raise Exception("No diagnostic response available. Run Send diagReq first.")
        actual=self.last_resp
        print(f"Diagnostic response: {actual}")
        return actual
    
    @keyword("Validate diagresp")
    def val_rsp(self,expected_resp):
        if not hasattr(self, "last_resp"):
            raise Exception("No diagnostic response available. Run Send diagReq first.")
        actual =self.last_resp.strip().split()
        expected = expected_resp.strip().split()
        if len(expected) > len(actual):
            raise Exception(f"Expected response has more bytes than actual response")
        for i in range(len(expected)):
            if expected[i].upper() == "XX":
                continue
            if actual[i].upper() != expected[i].upper():
                print(f"Diagnostic response: {self.last_resp}")
                raise Exception(f"Mismatch at byte {i}: expected {expected[i]} but got {actual[i]}" )
        print(f"[PASS] Diagnostic response matched: {' '.join(actual)}")
    
    @keyword("Validate Env_var value")
    def val_envar(self,env_var_name,expected_value):
        if env_var_name is None or expected_value is None:
            raise Exception("env_var_name,expected_Value both are required")
        value=self.canoe.get_environment_variable_value(env_var_name)
        if float(value)!=float(expected_value):
            raise Exception(f"Variable {env_var_name} expected {expected_value} but got {value}")
        print(f"[PASS] {env_var_name} == {expected_value}")
    
    @keyword("Validate Sys_var value")
    def val_sysvar(self,sys_var_name,expected_value):
        if sys_var_name is None or expected_value is None:
            raise Exception("env_var_name,expected_Value both are required")
        value=self.canoe.get_system_variable_value(sys_var_name)
        if float(value)!=float(expected_value):
            raise Exception(f"Variable {sys_var_name} expected {expected_value} but got {value}")
        print(f"[PASS] {sys_var_name} == {expected_value}")
   
    @keyword("Generate DBC Resource")
    def generate_dbc_resource(self, dbc_path):
        db = cantools.database.load_file(dbc_path)
        base_name = os.path.splitext(os.path.basename(dbc_path))[0]
        output_dir = "Resources"  
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{base_name}.resource")
        with open(output_file, "w") as f:
            f.write("*** Variables ***\n\n")
            for msg in db.messages:
                f.write(f"${{MSG_{msg.name.upper()}}}    {msg.name}\n")
                for sig in msg.signals:
                    f.write(f"${{SIG_{sig.name.upper()}}}    {sig.name}\n")
        print(f"[INFO] Resource file generated: {output_file}")
    
    @keyword("Save Configuration")
    def save_cfg(self):
        canoe_app=win32com.client.Dispatch("CANoe.Application")
        canoe_app.Configuration.Save()
        print(f"[INF0] Configurarion Saved")
    
    @keyword("Capture Image")
    def image_cmp(self,ref_img_path):
        cap=cv2.VideoCapture(0)
        ret,frame=cap.read()
        folder_path= os.path.join(os.getcwd(),"Capture Images")
        os.makedirs(folder_path,exist_ok=True)
        if ret:
            cv2.imwrite(os.path.join(folder_path, "Actual.png"),frame)
        else:
            print("Failed to capture image")
        r=cv2.imread(ref_img_path,cv2.IMREAD_COLOR)
        a=cv2.imread(os.path.join(folder_path, "Actual.png"),cv2.IMREAD_COLOR)
        r_gray=cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
        a_gray=cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        diff=cv2.absdiff(a_gray,r_gray)
        mean_diff=np.mean(diff)
        cv2.putText(r,'Reference Image',(40,80), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), 4)
        cv2.putText(a,'Actual Image',(40,80), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 255), 4)
        if mean_diff<2:
            print("Images are same")
            result=True
        else:
            print('Mismatch occured in images')
            result=False
            _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                if w * h < 500:
                    continue 
                #cv2.rectangle(r, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.rectangle(a, (x, y), (x + w, y + h), (0, 255, 0), 3)
        now=datetime.now()
        s_by_s=np.hstack((r,a))
        result_path= os.path.join(os.getcwd(),"Comparison Images")
        os.makedirs(result_path,exist_ok=True)
        path=os.path.join(result_path,f"comparison_Image_{now.strftime("%Y%m%d_%H%M%S")}.png")
        cv2.imwrite(path,s_by_s)
        time.sleep(3)
        logger.info(f'<img src="file:///{path}" width="400">', html=True)
        if not result:
            raise Failure("Image comparison failed")
        return result,path