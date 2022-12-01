from typing import TypedDict, List
import base64
import requests
import os

session = requests.Session()

# УЧРЕДИТЕЛИ-ЮЛ
class CompanyFoundersUl(TypedDict): 
    inn: str # ИНН
    ogrn: str # ОГРН
    share: int # Доля в уставном капитале


class Adapter_LoanRequest:
    
    json_api = {}
    
    loan_request = None
    
    def __init__(self, loan_request) -> None:
        self.loan_request = loan_request
        self.json_api = {
        "initiator": { # Инициатор заявки
            "phoneNumber": "" # Номер телефона
        },
        "company": { # Клиент
            "inn": "", # ИНН
            "ogrn": "", # ОГРН
            "shortNameEn": "", # Наименование на иностранном языке (если имеется)
            "legalAddress": "", # Юридический адрес компании
            "postalAddress": "", # Почтовый адрес компании
            "companyContacts": { # Контактные данные организации
                "email": "", # E-mail
                "phone": "", # Телефон
                "webSite": "", # Доменное имя, указатель страницы сайта в сети "Интернет", с использованием которых юридическим лицом оказываются услуги
                "fax": "" # Факс
            },
            "companyFoundersUl": [ # УЧРЕДИТЕЛИ-ЮЛ
                {
                    "inn": "", # ИНН
                    "ogrn": "", # ОГРН
                    "share": 0 # Доля в уставном капитале
                }
            ],
            "companyPersons": [ # СВЕДЕНИЯ О ФИЗИЧЕСКИХ ЛИЦАХ ОРГАНИЗАЦИИ
                {
                    "inn": "", # ИНН
                    "lastName": "", # Фамилия
                    "firstName": "", # Имя
                    "middleName": "", # Отчество
                    "gender": "", # Пол
                    "birthDate": "", # Дата рождения
                    "birthPlace": "", # Место рождения
                    "identityDocument": { # Документ, удостверяющий личность
                        "type": "", # Тип документа (выбор из справочника)
                        "series": "", # Серия
                        "number": "", # Номер
                        "issuedDate": "", # Дата выдачи
                        "issuingAuthority": "", # Кем выдан
                        "issuingAuthorityCode": "" # Код подразделения
                    },
                    "citizenship": "", # Гражданство (выбор из справочника)
                    "countryOfResidence": "", # Страна проживания (выбор из справочника)
                    "registrationAddress": "", # Адрес регистрации
                    "actualAddress": "", # Адрес местонахождения
                    "contacts": { # Контактные данные
                        "phone": "", # Телефон
                        "email": "" # Электронная почта
                    },
                    "roles": { # Роли физического лица в организации
                        "companyHead": { # ЕИО
                            "enabled": True,
                            "position": "" # Должность
                        },
                        "founder": { # Акционер/Учредитель
                            "enabled": True,
                            "share": 0 # Доля
                        },
                        "beneficiary": { # Бенифициар
                            "enabled": True,
                            "share": 0 # Доля
                        },
                        "signer": { # Подписант
                            "enabled": True,
                            "position": "" # Должность
                            # Действует по доверенности
                            # Информация о доверенности подписанта
                            #   Наименование документа
                            #   Номер документа
                            #   Дата доверенности
                            #   Дата окончания действия
                        }
                    },
                    "pdl": { # Отношение к публичным должностным лицам
                        "ipdl": True, # Является ИПДЛ
                        "mpdl": True, # Является МПДЛ
                        "rpdl": True # Является РПДЛ
                    }
                }
            ],
            "companyManagement": { # СТРУКТУРА ОРГАНОВ УПРАВЛЕНИЯ
                "supremeGoverningBody": "" # Высший орган управления (выбор из справочника)
            }
        },
        "companyBusinessInfo": { # ИНФОРМАЦИЯ О БИЗНЕСЕ
            "hasBeneficiariesInfo": True, # Сведения о выгодоприобретателях
            "beneficiariesInfo": "", # Укажите третьи лица, к выгоде которых действует компания
            "companyCarriesOutActivitiesSubjectToLicensing": "", # Компания осуществляет деятельность, подлежащую лицензированию (выбор из справочника)
            "historyReputationMarketSectorCompetition": "", # История, репутация, сектор рынка и конкуренция (выбор из справочника)
            "totalNumberOfTransactionsPerMonth": "", # Общее количество операций в месяц (выбор из справочника)
            "totalNumberOfTransactionsPerWeek": "", # Общее количество операций в неделю
            "totalNumberOfTransactionsPerQuarter": "", # Общее количество операций в квартал
            "totalNumberOfTransactionsPerYear": "", # Общее количество операций в год
            "totalSumTransactionsPerMonth": "", # Общая сумма операций в месяц (выбор из справочника)
            "totalSumTransactionsPerWeek": "", # Общая сумма операций в неделю
            "totalSumTransactionsPerQuarter": "", # Общая сумма операций в квартал
            "totalSumTransactionsPerYear": "", # Общая сумма операций в год
            "numberOfCashWithdrawalsPerMonth": "", # Количество операций по снятию наличности в месяц (выбор из справочника)
            "numberOfCashWithdrawalsPerWeek": "", # Количество операций по снятию наличности в неделю
            "numberOfCashWithdrawalsPerQuarter": "", # Количество операций по снятию наличности в квартал
            "numberOfCashWithdrawalsPerYear": "", # Количество операций по снятию наличности в год
            "amountOfCashWithdrawalsPerMonth": "", # Сумма операций по снятию наличности в месяц (руб.) (выбор из справочника)
            "amountOfCashWithdrawalsPerWeek": "", # Сумма операций по снятию денежных средств в наличной форме в неделю
            "amountOfCashWithdrawalsPerQuarter": "", # Сумма операций по снятию денежных средств в наличной форме в квартал
            "amountOfCashWithdrawalsPerYear": "", # Сумма операций по снятию денежных средств в наличной форме в год
            "numberTransactionsOnForeignTradeContractsPerMonth": "", # Количество операций по внешнеторговым контрактам в месяц (выбор из справочника)
            "numberTransactionsOnForeignTradeContractsPerWeek": "", # Количество операций по внешнеторговым контрактам в неделю
            "numberTransactionsOnForeignTradeContractsPerQuarter": "", # Количество операций по внешнеторговым контрактам в квартал
            "numberTransactionsOnForeignTradeContractsPerYear": "", # Количество операций по внешнеторговым контрактам в год
            "amountOfTransactionsUnderForeignTradeContractsPerMonth": "", # Сумма операций по внешнеторговым контрактам в месяц (руб.) (выбор из справочника)
            "amountOfTransactionsUnderForeignTradeContractsPerWeek": "", # Сумма операций по внешнеторговым контрактам в неделю
            "amountOfTransactionsUnderForeignTradeContractsPerQuarter": "", # Сумма операций по внешнеторговым контрактам в квартал
            "amountOfTransactionsUnderForeignTradeContractsPerYear": "", # Сумма операций по внешнеторговым контрактам в год
            "moneySources": "", # Источники происхождения денежных средств (выбор из справочника)
            "numberOfEmployees": "", # Штатная численность сотрудников (выбор из справочника)
            "selectAllTrueStatements": "" # Отметьте все верные утверждения (множественный выбор из справочника)
        },
        "typesOfContracts": { # ВИДЫ ДОГОВОРОВ (КОНТРАКТОВ), РАСЧЕТЫ ПО КОТОРЫМ ЮРИДИЧЕСКОЕ ЛИЦО СОБИРАЕТСЯ ОСУЩЕСТВЛЯТЬ ЧЕРЕЗ БАНК
            "contractProvisionServices": True, # Договор возмездного оказания услуг
            "supplyContract": True, # Договор поставки
            "workAgreement": True, # Договор подряда
            "commissionAgreement": True, # Договор комиссии
            "contractOfSale": True, # Договор купли-продажи
            "leaseAgreementForMovableProperty": True, # Договор аренды движимого имущества
            "realEstateLeaseAgreement": True, # Договор аренды недвижимого имущества
            "leasingAgreement": True, # Договор лизинга
            "factoringAgreement": True, # Договор факторинга
            "other": True, # Иное
            "contractsInfo": "" # Иные виды договоров
        },
        "additionalProducts": { # ДОПОЛНИТЕЛЬНЫЕ ПРОДУКТЫ К ПОДКЛЮЧЕНИЮ
            "sms": True, # СМС-оповещение
            "overdraft": True, # Овердрафт
            "internetAcquiring": True, # Интернет-эквайринг
            "merchantAcquiring": True, # Торговый эквайринг
            "fastPaymentSystem": True, # Расчеты по Системе быстрых платежей
            "loyaltyProgram": True, # Подключить к Программе лояльности
            "loyaltyProgramInfo": "", # Программа лояльности (выбор из справочника)
            "community": True, # Комьюнити
            "accounting": True, # Бухгалтерия
            "legalSupport": True, # Юридическая поддержка
            "promotion": True # Продвижение
        },
        "consents": { # Согласия
            "consentPd": True, # Согласие на обработку персональных данных
            "consentBki": True, # Согласие для бюро кредитных историй
            "consentToReceiveInfoLetters": True, # Согласие на получение информационной рассылки
            "consentSubscriberInformation": True, # Согласие на обработку сведений об абоненте
            "confirmationAccessionToTermsOfPEPFL": True, # Подтверждение присоединения к Соглашению ПЭП ФЛ
            "confirmationAccessionToTermsOfGuarantor": True # Подтверждение присоединения к Условиям поручительства
        },
        "selectedTariff": "", # Выбранный ТАРИФ НА РАСЧЕТНО-КАССОВОЕ ОБСЛУЖИВАНИЕ 
        "codeword": "", # Кодовое слово
        "documents": [
            {
                "docType": "", # Тип документа (справочник)
                "files": [
                    {
                        "fileName": "",
                        "content": ""
                    }
                ]
            }
        ]
    }
    
    def getInitiatorData(self, phoneNumber) -> dict:
        return {
            "phoneNumber": phoneNumber, # Номер телефона
        }

    def setInitiator(self, initiator) -> None:
        self.json_api['initiator'] = initiator


    def getCompanyBase(self, inn, ogrn, shortNameEn, legalAddress, postalAddress) -> dict:
        return {
            "inn": inn, # ИНН
            "ogrn": ogrn, # ОГРН
            "shortNameEn": shortNameEn, # Наименование на иностранном языке (если имеется)
            "legalAddress": legalAddress, # Юридический адрес компании
            "postalAddress": postalAddress, # Почтовый адрес компании
        }

    def getCompanyContacts(self, email, phone, webSite, fax) -> dict:
        return {
            "companyContacts": { # Контактные данные организации
                "email": email, # E-mail
                "phone": phone, # Телефон
                "webSite": webSite, # Доменное имя, указатель страницы сайта в сети "Интернет", с использованием которых юридическим лицом оказываются услуги
                "fax": fax, # Факс
            },
        }

    def getCompanyFoundersUl(self, companyFoundersUl: List[CompanyFoundersUl]) -> dict:
        return {
            "companyFoundersUl": companyFoundersUl,
        }


    def getCompanyPersonsBase(self, inn, lastName, firstName, middleName, gender, birthDate, birthPlace, citizenship, countryOfResidence, registrationAddress, actualAddress):
        return {
            "inn": inn, # ИНН
            "lastName": lastName, # Фамилия
            "firstName": firstName, # Имя
            "middleName": middleName, # Отчество
            "gender": gender, # Пол
            "birthDate": birthDate, # Дата рождения
            "birthPlace": birthPlace, # Место рождения
            "citizenship": citizenship, # Гражданство (выбор из справочника)
            "countryOfResidence": countryOfResidence, # Страна проживания (выбор из справочника)
            "registrationAddress": registrationAddress, # Адрес регистрации
            "actualAddress": actualAddress, # Адрес местонахождения
        }

    def getContacts(self, phone, email):
        return {
            "contacts": { # Контактные данные
                "phone": phone, # Телефон
                "email": email # Электронная почта
            },
        }

    def getIdentityDocument(self, type, series, number, issuedDate, issuingAuthority, issuingAuthorityCode):
        return {
            "identityDocument": { # Документ, удостверяющий личность
                "type": type, # Тип документа (выбор из справочника)
                "series": series, # Серия
                "number": number, # Номер
                "issuedDate": issuedDate, # Дата выдачи
                "issuingAuthority": issuingAuthority, # Кем выдан
                "issuingAuthorityCode": issuingAuthorityCode, # Код подразделения
            },
        }

    def getRoles(self, roles, companyHeadPosition, founderShare, beneficiaryShare, signerPosition):
        companyHeadEnabled = False
        founderEnabled = False
        beneficiaryEnabled = False
        signerEnabled = False
        
        if 'Учредитель' in roles:
            founderEnabled = True
        
        if 'Бенефициарный владелец' in roles:
            beneficiaryEnabled = True
        
        if 'Подписант' in roles:
            signerEnabled = True
        
        if 'Руководитель' in roles:
            companyHeadEnabled = True

        return {
            "roles": { # Роли физического лица в организации
                "companyHead": { # ЕИО
                    "enabled": companyHeadEnabled,
                    "position": companyHeadPosition # Должность
                },
                "founder": { # Акционер/Учредитель
                    "enabled": founderEnabled,
                    "share": founderShare # Доля
                },
                "beneficiary": { # Бенифициар
                    "enabled": beneficiaryEnabled,
                    "share": beneficiaryShare # Доля
                },
                "signer": { # Подписант
                    "enabled": signerEnabled,
                    "position": signerPosition # Должность
                    # Действует по доверенности
                    # Информация о доверенности подписанта
                    #   Наименование документа
                    #   Номер документа
                    #   Дата доверенности
                    #   Дата окончания действия
                }
            },
        }

    def getPdl(self, ipdl, mpdl, rpdl):
        return {
            "pdl": { # Отношение к публичным должностным лицам
                "ipdl": ipdl, # Является ИПДЛ
                "mpdl": mpdl, # Является МПДЛ
                "rpdl": rpdl # Является РПДЛ
            }
        }

    def getCompanyPersons(self, companyPersonsBase, identityDocument, contacts, roles, pdl):
        return {
            **companyPersonsBase,
            **identityDocument,
            **contacts,
            **roles,
            **pdl,
        }
    
    def getCompanyManagement(self, supremeGoverningBody):
        return {
            "companyManagement": { # СТРУКТУРА ОРГАНОВ УПРАВЛЕНИЯ
                "supremeGoverningBody": supremeGoverningBody # Высший орган управления (выбор из справочника)
            }
        }

    def setTariff(self, tariff):
        self.json_api['selectedTariff'] = tariff

    def getLoadRequest_legalAddress(self):
        lr = self.loan_request
        addresses = lr.addresses
        for address in addresses:
            if "Юридический" in address['type_adress']:
                return address['address']
        return ""

    def getLoadRequest_postalAddress(self):
        lr = self.loan_request
        addresses = lr.addresses
        for address in addresses:
            if "Почтовый" in address['type_adress']:
                return address['address']
        return ""


    def parserCompanyPersons(self):
        companyPersons = []
        for persons in self.loan_request.list_supervisoty_board_persone:
            companyPersonsData = {}
            for key in persons:
                page = persons[key]
                companyPersonsData = {**companyPersonsData,  **page}
            companyPersons.append(companyPersonsData)
        for persons in self.loan_request.list_collegial_executive_body:
            companyPersonsData = {}
            for key in persons:
                page = persons[key]
                companyPersonsData = {**companyPersonsData,  **page}
            companyPersons.append(companyPersonsData)
        return companyPersons

    def setCompany(self, company):
        self.json_api['company'] = company
    
    def setDocument(self, listObj):
        self.json_api['documents'] = listObj
    
    def getDocument(self, url):
        response = session.get(os.getenv("DJANGO_APP_DOMAIN_STORAGE") + url)
        uri = ("data:" + response.headers['Content-Type'] + ";" + "base64," + base64.b64encode(response.content).decode("utf-8"))
        nameFile = url.split('/')[-1]

        return {
                "docType": response.headers['Content-Type'], # Тип документа (справочник)
                "files": [
                    {
                        "fileName": nameFile,
                        "content": uri
                    }
                ]
            }
        

    def getResult(self):
        lr = self.loan_request
        initiatorData = self.getInitiatorData(phoneNumber=lr.contact_number)
        self.setInitiator(initiator=initiatorData)
        
        legalAddress = self.getLoadRequest_legalAddress()
        postalAddress = self.getLoadRequest_postalAddress()

        companyBase = self.getCompanyBase(
            inn=lr.inn,
            ogrn="",
            shortNameEn="",
            legalAddress=legalAddress,
            postalAddress=postalAddress,
        )
        companyContacts = self.getCompanyContacts(
            email="",
            phone=lr.contact_number,
            webSite="",
            fax="",
        )
        companyFoundersUl = self.getCompanyFoundersUl([])
        
        lr_list_companyPersons = self.parserCompanyPersons()
        companyPersonsList = []
        documentList = []
        for lr_persons in lr_list_companyPersons:
            print(lr_persons)
            companyPersonsBase = self.getCompanyPersonsBase(
                inn=lr_persons['account_onw_inn'],
                lastName=lr_persons['account_own_name'],
                firstName=lr_persons['account_own_lastname'],
                middleName=lr_persons['account_own_surname'],
                gender=lr_persons['account_own_gender'],
                birthDate=lr_persons['account_datebirth'],
                birthPlace=lr_persons['account_birth_place'],
                citizenship="",
                countryOfResidence="",
                registrationAddress="",
                actualAddress="",
            )

            companyContact = self.getContacts(
                phone="",
                email="",
            )

            identityDocument = self.getIdentityDocument(
                type=lr_persons['doc_type'],
                series=lr_persons['doc_serial'],
                number=lr_persons['doc_number'],
                issuedDate=lr_persons['date_issue'],
                issuingAuthority=lr_persons['issued_by'],
                issuingAuthorityCode=lr_persons['division_code'],
            )

            roles = self.getRoles(
                roles=lr_persons['account_onw_role'],
                companyHeadPosition="",
                founderShare=0,
                beneficiaryShare=0,
                signerPosition="",
            )

            pdl = self.getPdl(
                ipdl="",
                mpdl="",
                rpdl="",
            )

            companyPersons = self.getCompanyPersons(
                companyPersonsBase=companyPersonsBase,
                identityDocument=identityDocument,
                contacts=companyContact,
                roles=roles,
                pdl=pdl,
            )
            
            document = self.getDocument(url=lr_persons['first_passport_page_url'])
            documentList.append(document)

            companyPersonsList.append(companyPersons)
        
        companyManagement = self.getCompanyManagement(
            supremeGoverningBody=lr.supreme_management_body
        )
        self.setCompany(
            {
                "companyPersons": companyPersonsList,
                **companyBase,
                **companyContacts,
                **companyFoundersUl,
                **companyManagement,
            }
        )
        self.setTariff(
            lr.tariff
        )

        self.setDocument(documentList)

        return self.json_api
