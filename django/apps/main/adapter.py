from typing import TypedDict, List


# УЧРЕДИТЕЛИ-ЮЛ
class CompanyFoundersUl(TypedDict): 
    inn: str # ИНН
    ogrn: str # ОГРН
    share: int # Доля в уставном капитале


class Adapter_LoanRequest:
    
    json_api = {
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
    
    loan_request = None
    
    def __init__(self, loan_request) -> None:
        self.loan_request = loan_request
    
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

    def getRoles(self, companyHeadEnabled, companyHeadPosition, founderEnabled, founderShare, beneficiaryEnabled, beneficiaryShare, signerEnabled, signerPosition):
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

    def getCompanyPersons(self, companyPersonsBase, identityDocument, сontacts, roles, pdl):
        return {
            **companyPersonsBase,
            **identityDocument,
            **сontacts,
            **roles,
            **pdl,
        }
    
    def getCompanyManagement(self, supremeGoverningBody):
        return {
            "companyManagement": { # СТРУКТУРА ОРГАНОВ УПРАВЛЕНИЯ
                "supremeGoverningBody": supremeGoverningBody # Высший орган управления (выбор из справочника)
            }
        }


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
        сompanyContacts = self.getCompanyContacts(
            email="",
            phone=lr.contact_number,
            webSite="",
            fax="",
        )
        companyFoundersUl = self.getCompanyFoundersUl([])
        
        companyPersons = self.parserCompanyPersons()
        
        
        print(companyPersons)
        return self.json_api
