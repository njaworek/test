*** Settings ***
Library   SSHLibrary
Library   Selenium2Library

*** Variables ***
${MESSAGE}  Hello Tester, have a good day!
${REMOTE_HOST}    127.0.0.1
${USERNAME}   tester
${PASSWORD}   tester
${Uname}
${USERNAMEWP}    //*[@id="login"]
${PASSWORDWP}      //*[@id="password"]
${BUTTONWP}    //*[@id="btnSubmit"]
${USER}   testerwsb_t1
${PASSWORDUSER}   adam1234

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
6 Otworzenie strony z poczta WP
    Otworzenie przegladarki
    Wpisanie adresu poczta.wp.pl i przejscie na strone
    Wprowadzenie poprawnego loginu
    Wprowadzenie poprawnego hasla
    Zaloguj sie
    Sprawdzenie czy zostalismy zalogowanie
    Zamkniecie przegladarki


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
  Should not be empty   ${Uname}
  Should Contain    ${Uname}    Linux
Zamknij polaczenie
  Close Connection
Otworzenie przegladarki
  Open Browser    http://wp.pl
Wpisanie adresu poczta.wp.pl i przejscie na strone
  Go To     http://poczta.wp.pl
Wprowadzenie poprawnego loginu
  Input Text    ${USERNAMEWP}      ${USER}
Wprowadzenie poprawnego hasla
  Input Text     ${PASSWORDWP}    ${PASSWORDUSER}
Zaloguj sie
  Click Button    ${BUTTONWP}
Sprawdzenie czy zostalismy zalogowanie
  PAGE SHOULD Contain   Odebrane
Zamkniecie przegladarki
  CLose Browser
