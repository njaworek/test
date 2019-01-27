*** Settings ***
Library   Selenium2Library

*** Variables ***
${USERNAMEWP}   //*[@id="login"]
${PASSWORDWP}    //*[@id="password"]
${BUTTONWP}   //*[@id="btnSubmit"]
${USER}   testerwsb_t1
${PASSWORDUSER}   adam1234

*** Test Cases ***
1 Otworzenie strony z poczta WP
    Otworzenie przegladarki
    Wpisanie adresu poczta.wp.pl i przejscie na strone
    Wprowadzenie poprawnego loginu
    Wprowadzenie poprawnego hasla
    Zaloguj sie
    Sprawdzenie czy zostalismy zalogowanie
    Zamkniecie przegladarki

*** Keywords ***
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
