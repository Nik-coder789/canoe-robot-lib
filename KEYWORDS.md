# 🔑 CANoe Robot Library Keywords

This document describes all available keywords and their usage.

---

## 📦 Generate DBC Resource

Generates a Robot Framework `.resource` file from a DBC file.
This will give a drop down of your Msgs & signals while writing Test cases.

Arguments:

* dbc_path (str): Path to DBC file

Returns:

* Resource file -- include that resource file in your robot file as below
* Resource  ../Resources/Generated_file.resource

---

## ▶️ Start CANoe

Start CANoe with given configuration file.

Arguments:

* cfg_path (str): Path to CANoe configuration file

---

## ⏹️ Stop CANoe

Stops CANoe measurement.

---

## 📡 Get Signal

Reads a signal value from CAN bus.

Arguments:

* Bus (str) - CAN, LIN etc..
* Channel (int)
* Message name (str)
* Signal name (str)

Returns:

* Signal value

---

## ✏️ Set Signal

Writes value to a CAN signal.

Arguments:

* Bus (str) - CAN, LIN etc..
* Channel (int)
* Message name (str)
* Signal name (str)
* value

---

## 🔍 Send diagReq

Sends diagnostic request to ECU.

Arguments:

* Ecu_qualifier_name (str)
* Request (str)

---

## 🌐 Set Environment_Variable

Sets environment variable value.

Arguments:

* env_var_name (str)
* value

---

## 🌐 Get Environment_Variable

Reads environment variable value.

Arguments:

* env_var_name (str)

Returns:

* value

---

## ⚙️ Set SysVar_Value

Sets system variable.

Arguments:

* sys_var_name (str)
* value

---

## ⚙️ Get SysVar_Value

Reads system variable.

Arguments:

* sys_var_name (str)

Returns:

* value

---

## 🔁 Set Replay_block

Assigns BLF file to replay block.

Arguments:

* block_name (str)
* recording_file_path (str)

---

## ▶️ Run Replay_block

Starts or stops replay block.

Arguments:

* block_name (str)
* start_stop (bool)

---

## 🧪 Execute Test_Module

Executes a CANoe test module.

Arguments:

* test_module_name (str)

---

## 🧪 Execute Test Environement

Executes all test modules in given environment.

Arguments:

* test_environment_name (str)

---

## 🧪 Execute all Test_env

Executes all test environments.

---

## 📝 Write

Writes text in CANoe Write Window.

Arguments:

* text (str)

---

## 📡 Validate Signal value

Validates whether a signal matches the expected value.

Arguments:

* bus (str)
* channel (int)
* message (str)
* signal (str)
* expected_value

Behavior:

* Passes if signal value matches expected value
* Fails if mismatch

---

## 🔍 Get diagresp

Returns the last diagnostic response received.

Usage:

* Must be used after `Send diagReq`

Returns:

* Diagnostic response

---

## 🔍 Validate diagresp

Validates the diagnostic response against expected value.

Arguments:

* expected_resp (str)

Behavior:

* Passes if response matches
* Fails if mismatch

---

## 🌐 Validate Env_var value

Validates environment variable value.

Arguments:

* env_var_name (str)
* expected_value

Behavior:

* Passes if value matches
* Fails if mismatch

---

## ⚙️ Validate Sys_var value

Validates system variable value.

Arguments:

* sys_var_name (str)
* expected_value

Behavior:

* Passes if value matches
* Fails if mismatch
