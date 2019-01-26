*** Settings ***
Library   SSHLibrary

*** Variables ***
${MESSAGE}  Hello Tester, have a good day!
${REMOTE_HOST}    127.0.0.1
${USERNAME}   tester
${PASSWORD}   tester
${Uname}

*** Test Cases ***
1 Test log to Console
    Log To Console    Hello, console!
2 Test log
    Log
3 Test about my log
    My Log    ${MESSAGE}
4 Log in and open connection
    Open Connection     ${REMOTE_HOST}
    Login    ${USERNAME}    ${PASSWORD}
5 Testing parameters of command uname
    Otworz polaczenie z komputerem
    Zaloguj sie z poprawnymi userem i haslem
    Napisz komende i sprawdz poprawnosc
    Zamknij polaczenie


*** Keywords ***
Log
  Log To Console    Hello, console!
My Log
  [Arguments]   ${MESSAGE}
  Log To Console    ${MESSAGE}
Otworz polaczenie z komputerem
  Open Connection   ${REMOTE_HOST}
Zaloguj sie z poprawnymi userem i haslem
  Login   ${USERNAME}   ${PASSWORD}
Napisz komende i sprawdz poprawnosc
  ${Uname}=   Execute command    uname -a
  Should not be empty   ${Uname}+
  Should Contain    ${Uname}    Linux
Zamknij polaczenie
  Close Connection
