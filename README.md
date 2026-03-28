# 🚗 CANoe Robot Framework Library

A custom Robot Framework library for automating CANoe using Python.

This library provides reusable keywords to control CANoe, interact with CAN signals, perform diagnostics, manage replay blocks, handle environment/system variables, and execute test modules.

---

## 📦 Installation

pip install canoe-robot-lib

---

## ⚙️ Requirements

* Python 3.7+
* Robot Framework
* py_canoe library
* CANoe installed (Vector tool)
* Valid CANoe license

---

## 📂 Usage

Import the library in your Robot Framework test file:

*** Settings ***
Library    canoe_robot_lib.keywords.CanoeLibrary

---

## 🧪 Example Test Case

*** Variables ***
${cfg}    path_to_cfg_file.cfg

*** Test Cases ***
Basic CANoe Test
Start CANoe    ${cfg}
Set Signal     CAN    1    Msg    Signal    1
${val}=        Get Signal    CAN    1    Msg    Signal
Should Be Equal As Numbers    ${val}    1
Stop CANoe

---

## 📘 Keywords Documentation

Detailed keyword descriptions are available in:

➡️ KEYWORDS.md

---

## 📌 Notes

* CANoe configuration (.cfg) must be valid before execution
* User should have knowledge of CANoe setup (signals, DBC, test modules)
* Boolean inputs (True/False) are used for control keywords like replay
* Some features depend on CANoe configuration setup

---

## 👨‍💻 Author

Naresh Kothari
System Test Engineer – Automotive Domain

---

## 📄 License

This project is for learning and development purposes.
