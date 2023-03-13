from typing import TypedDict, List
from .utils import format_date, format_string
import base64
import requests
import os

session = requests.Session()

# УЧРЕДИТЕЛИ-ЮЛ


class CompanyFoundersUl(TypedDict):
    inn: str  # ИНН
    ogrn: str  # ОГРН
    share: int  # Доля в уставном капитале


class Adapter_LoanRequest:

    json_api = {}

    loan_request = None

    def __init__(self, loan_request) -> None:
        self.loan_request = loan_request
        self.json_api = {
            "initiator": {  # Инициатор заявки
                "phoneNumber": ""  # Номер телефона
            },
            "isEioPDL": True,
            "company": {  # Клиент
                "inn": "",  # ИНН
                "ogrn": "",  # ОГРН
                "shortName": "",
                # Наименование на иностранном языке (если имеется)
                "shortNameEn": "",
                "legalAddress": "",  # Юридический адрес компании
                "postalAddress": "",  # Почтовый адрес компании
                "companyContacts": {  # Контактные данные организации
                    "email": "",  # E-mail
                    "phone": "",  # Телефон
                    "webSite": "",  # Доменное имя, указатель страницы сайта в сети "Интернет", с использованием которых юридическим лицом оказываются услуги
                    "fax": ""  # Факс
                },
                "companyFoundersUl": [  # УЧРЕДИТЕЛИ-ЮЛ
                    {
                        "inn": "",  # ИНН
                        "ogrn": "",  # ОГРН
                        "share": 0  # Доля в уставном капитале
                    }
                ],
                "companyPersons": [  # СВЕДЕНИЯ О ФИЗИЧЕСКИХ ЛИЦАХ ОРГАНИЗАЦИИ
                    {
                        "inn": "",  # ИНН
                        "lastName": "",  # Фамилия
                        "firstName": "",  # Имя
                        "middleName": "",  # Отчество
                        "gender": "",  # Пол
                        "birthDate": "",  # Дата рождения
                        "birthPlace": "",  # Место рождения
                        "identityDocument": {  # Документ, удостверяющий личность
                            "type": "",  # Тип документа (выбор из справочника)
                            "series": "",  # Серия
                            "number": "",  # Номер
                            "issuedDate": "",  # Дата выдачи
                            "issuingAuthority": "",  # Кем выдан
                            "issuingAuthorityCode": ""  # Код подразделения
                        },
                        # Гражданство (выбор из справочника)
                        "citizenship": "",
                        # Страна проживания (выбор из справочника)
                        "countryOfResidence": "",
                        "registrationAddress": "",  # Адрес регистрации
                        "actualAddress": "",  # Адрес местонахождения
                        "contacts": {  # Контактные данные
                            "phone": "",  # Телефон
                            "email": ""  # Электронная почта
                        },
                        "roles": {  # Роли физического лица в организации
                            "companyHead": {  # ЕИО
                                "enabled": True,
                                "position": ""  # Должность
                            },
                            "founder": {  # Акционер/Учредитель
                                "enabled": True,
                                "share": 0  # Доля
                            },
                            "beneficiary": {  # Бенифициар
                                "enabled": True,
                                "share": 0  # Доля
                            },
                        },
                        "pdl": {  # Отношение к публичным должностным лицам
                            "ipdl": True,  # Является ИПДЛ
                            "mpdl": True,  # Является МПДЛ
                            "rpdl": True  # Является РПДЛ
                        }
                    }
                ],
                "companyManagement": {  # СТРУКТУРА ОРГАНОВ УПРАВЛЕНИЯ
                    # Высший орган управления (выбор из справочника)
                    "supremeGoverningBody": "",
                    "selectedManagementKey": None,
                }
            },
            "companyBusinessInfo": {  # ИНФОРМАЦИЯ О БИЗНЕСЕ
                "hasBeneficiariesInfo": True,  # Сведения о выгодоприобретателях
                "beneficiariesInfo": "",  # Укажите третьи лица, к выгоде которых действует компания
                # Компания осуществляет деятельность, подлежащую лицензированию (выбор из справочника)
                "companyCarriesOutActivitiesSubjectToLicensing": "",
                # История, репутация, сектор рынка и конкуренция (выбор из справочника)
                "historyReputationMarketSectorCompetition": "",
                # Общее количество операций в месяц (выбор из справочника)
                "totalNumberOfTransactionsPerMonth": "",
                "totalNumberOfTransactionsPerWeek": "",  # Общее количество операций в неделю
                # Общее количество операций в квартал
                "totalNumberOfTransactionsPerQuarter": "",
                "totalNumberOfTransactionsPerYear": "",  # Общее количество операций в год
                # Общая сумма операций в месяц (выбор из справочника)
                "totalSumTransactionsPerMonth": "",
                "totalSumTransactionsPerWeek": "",  # Общая сумма операций в неделю
                "totalSumTransactionsPerQuarter": "",  # Общая сумма операций в квартал
                "totalSumTransactionsPerYear": "",  # Общая сумма операций в год
                # Количество операций по снятию наличности в месяц (выбор из справочника)
                "numberOfCashWithdrawalsPerMonth": "",
                # Количество операций по снятию наличности в неделю
                "numberOfCashWithdrawalsPerWeek": "",
                # Количество операций по снятию наличности в квартал
                "numberOfCashWithdrawalsPerQuarter": "",
                # Количество операций по снятию наличности в год
                "numberOfCashWithdrawalsPerYear": "",
                # Сумма операций по снятию наличности в месяц (руб.) (выбор из справочника)
                "amountOfCashWithdrawalsPerMonth": "",
                # Сумма операций по снятию денежных средств в наличной форме в неделю
                "amountOfCashWithdrawalsPerWeek": "",
                # Сумма операций по снятию денежных средств в наличной форме в квартал
                "amountOfCashWithdrawalsPerQuarter": "",
                # Сумма операций по снятию денежных средств в наличной форме в год
                "amountOfCashWithdrawalsPerYear": "",
                # Количество операций по внешнеторговым контрактам в месяц (выбор из справочника)
                "numberTransactionsOnForeignTradeContractsPerMonth": "",
                # Количество операций по внешнеторговым контрактам в неделю
                "numberTransactionsOnForeignTradeContractsPerWeek": "",
                # Количество операций по внешнеторговым контрактам в квартал
                "numberTransactionsOnForeignTradeContractsPerQuarter": "",
                # Количество операций по внешнеторговым контрактам в год
                "numberTransactionsOnForeignTradeContractsPerYear": "",
                # Сумма операций по внешнеторговым контрактам в месяц (руб.) (выбор из справочника)
                "amountOfTransactionsUnderForeignTradeContractsPerMonth": "",
                # Сумма операций по внешнеторговым контрактам в неделю
                "amountOfTransactionsUnderForeignTradeContractsPerWeek": "",
                # Сумма операций по внешнеторговым контрактам в квартал
                "amountOfTransactionsUnderForeignTradeContractsPerQuarter": "",
                # Сумма операций по внешнеторговым контрактам в год
                "amountOfTransactionsUnderForeignTradeContractsPerYear": "",
                # Источники происхождения денежных средств (выбор из справочника)
                "moneySources": "",
                # Штатная численность сотрудников (выбор из справочника)
                "numberOfEmployees": "",
                "fatcaAndStrategicStatus": ""
            },
            "typesOfContracts": {  # ВИДЫ ДОГОВОРОВ (КОНТРАКТОВ), РАСЧЕТЫ ПО КОТОРЫМ ЮРИДИЧЕСКОЕ ЛИЦО СОБИРАЕТСЯ ОСУЩЕСТВЛЯТЬ ЧЕРЕЗ БАНК
                "contractProvisionServices": True,  # Договор возмездного оказания услуг
                "supplyContract": True,  # Договор поставки
                "workAgreement": True,  # Договор подряда
                "commissionAgreement": True,  # Договор комиссии
                "contractOfSale": True,  # Договор купли-продажи
                "leaseAgreementForMovableProperty": True,  # Договор аренды движимого имущества
                "realEstateLeaseAgreement": True,  # Договор аренды недвижимого имущества
                "leasingAgreement": True,  # Договор лизинга
                "factoringAgreement": True,  # Договор факторинга
                "other": True,  # Иное
                "contractsInfo": ""  # Иные виды договоров
            },
            "additionalProducts": {  # ДОПОЛНИТЕЛЬНЫЕ ПРОДУКТЫ К ПОДКЛЮЧЕНИЮ
                "sms": True,  # СМС-оповещение
                "overdraft": True,  # Овердрафт
                "internetAcquiring": True,  # Интернет-эквайринг
                "merchantAcquiring": True,  # Торговый эквайринг
                "fastPaymentSystem": True,  # Расчеты по Системе быстрых платежей
                "loyaltyProgram": True,  # Подключить к Программе лояльности
                # Программа лояльности (выбор из справочника)
                "loyaltyProgramInfo": "",
                "community": True,  # Комьюнити
                "accounting": True,  # Бухгалтерия
                "legalSupport": True,  # Юридическая поддержка
                "promotion": True  # Продвижение
            },
            "consents": {  # Согласия
                "consentPd": True,  # Согласие на обработку персональных данных
                "consentBki": True,  # Согласие для бюро кредитных историй
                # Согласие на получение информационной рассылки
                "consentToReceiveInfoLetters": True,
                # Согласие на обработку сведений об абоненте
                "consentSubscriberInformation": True,
                # Подтверждение присоединения к Соглашению ПЭП ФЛ
                "confirmationAccessionToTermsOfPEPFL": True,
                # Подтверждение присоединения к Условиям поручительства
                "confirmationAccessionToTermsOfGuarantor": True
            },
            "infoOnPurposesOfFinancialAndEconomicActivities": {
                "hasConstantPayers": True,
                "hasConstantPayersDetails": "hasConstantPayersDetails",
                "hasConstantRecipient": True,
                "hasConstantRecipientDetails": "hasConstantRecipientDetails"
            },
            "selectedTariff": "",  # Выбранный ТАРИФ НА РАСЧЕТНО-КАССОВОЕ ОБСЛУЖИВАНИЕ
            "codeword": "",  # Кодовое слово
            "documents": [],
        }

    # ВИДЫ ДОГОВОРОВ (КОНТРАКТОВ), РАСЧЕТЫ ПО КОТОРЫМ ЮРИДИЧЕСКОЕ ЛИЦО СОБИРАЕТСЯ ОСУЩЕСТВЛЯТЬ ЧЕРЕЗ БАНК
    def setTypesOfContracts(
        self,
        contractProvisionServices,
        supplyContract,
        workAgreement,
        commissionAgreement,
        contractOfSale,
        leaseAgreementForMovableProperty,
        realEstateLeaseAgreement,
        leasingAgreement,
        factoringAgreement,
        other,
        contractsInfo,
    ):
        self.json_api["typesOfContracts"] = {
            # Договор возмездного оказания услуг
            "contractProvisionServices": contractProvisionServices,
            "supplyContract": supplyContract,  # Договор поставки
            "workAgreement": workAgreement,  # Договор подряда
            "commissionAgreement": commissionAgreement,  # Договор комиссии
            "contractOfSale": contractOfSale,  # Договор купли-продажи
            # Договор аренды движимого имущества
            "leaseAgreementForMovableProperty": leaseAgreementForMovableProperty,
            # Договор аренды недвижимого имущества
            "realEstateLeaseAgreement": realEstateLeaseAgreement,
            "leasingAgreement": leasingAgreement,  # Договор лизинга
            "factoringAgreement": factoringAgreement,  # Договор факторинга
            "other": other,  # Иное
            "contractsInfo": contractsInfo  # Иные виды договоров
        }

    def getInitiatorData(self, phoneNumber) -> dict:
        return {
            "phoneNumber": phoneNumber,  # Номер телефона
        }

    def setInitiator(self, initiator) -> None:
        self.json_api['initiator'] = initiator

    def getCompanyBase(self, inn, ogrn, shortName, shortNameEn, legalAddress, postalAddress) -> dict:
        return {
            "inn": format_string(inn),  # ИНН
            "ogrn": format_string(ogrn),  # ОГРН
            # Наименование на иностранном языке (если имеется)
            "shortName": shortName,
            "shortNameEn": shortNameEn,
            "legalAddress": legalAddress,  # Юридический адрес компании
            "postalAddress": postalAddress,  # Почтовый адрес компании
        }

    def getCompanyContacts(self, email, phone, webSite, fax) -> dict:
        return {
            "companyContacts": {  # Контактные данные организации
                "email": email,  # E-mail
                "phone": phone,  # Телефон
                "webSite": webSite,  # Доменное имя, указатель страницы сайта в сети "Интернет", с использованием которых юридическим лицом оказываются услуги
                "fax": fax,  # Факс
            },
        }

    def getCompanyFoundersUl(self, companyFoundersUl: List[CompanyFoundersUl]) -> dict:
        return {
            "companyFoundersUl": companyFoundersUl,
        }

    def getCompanyPersonsBase(self, inn, lastName, firstName, middleName, gender, birthDate, birthPlace, citizenship, countryOfResidence, registrationAddress, actualAddress):
        return {
            "inn": format_string(inn),  # ИНН
            "lastName": lastName,  # Фамилия
            "firstName": firstName,  # Имя
            "middleName": middleName,  # Отчество
            "gender": gender,  # Пол
            "birthDate": format_date(birthDate),  # Дата рождения
            "birthPlace": birthPlace,  # Место рождения
            "citizenship": citizenship,  # Гражданство (выбор из справочника)
            # Страна проживания (выбор из справочника)
            "countryOfResidence": countryOfResidence,
            "registrationAddress": registrationAddress,  # Адрес регистрации
            "actualAddress": actualAddress,  # Адрес местонахождения
        }

    def getContacts(self, phone, email):
        return {
            "contacts": {  # Контактные данные
                "phone": format_string(phone),  # Телефон
                "email": email  # Электронная почта
            },
        }

    def getIdentityDocument(self, type, series, number, issuedDate, issuingAuthority, issuingAuthorityCode):
        return {
            "identityDocument": {  # Документ, удостверяющий личность
                "type": type,  # Тип документа (выбор из справочника)
                "series": format_string(series),  # Серия
                "number": format_string(number),  # Номер
                "issuedDate": format_date(issuedDate),  # Дата выдачи
                "issuingAuthority": issuingAuthority,  # Кем выдан
                "issuingAuthorityCode": issuingAuthorityCode,  # Код подразделения
            },
        }

    def getRoles(self, roles, companyHeadPosition="", founderShare=0, beneficiaryShare=0):
        companyHeadEnabled = False
        founderEnabled = False
        beneficiaryEnabled = False

        if 'ЕИО' in roles:
            companyHeadEnabled = True

        if 'Акционер/учредитель' in roles:
            founderEnabled = True

        if 'Бенифициар' in roles:
            beneficiaryEnabled = True

        return {
            "roles": {  # Роли физического лица в организации
                "companyHead": {  # ЕИО
                    "enabled": companyHeadEnabled,
                    "position": companyHeadPosition  # Должность
                },
                "founder": {  # Акционер/Учредитель
                    "enabled": founderEnabled,
                    "share": founderShare  # Доля
                },
                "beneficiary": {  # Бенифициар
                    "enabled": beneficiaryEnabled,
                    "share": beneficiaryShare  # Доля
                },
            },
        }

    def getPdl(self, ipdl, mpdl, rpdl):
        return {
            "pdl": {  # Отношение к публичным должностным лицам
                "ipdl": ipdl,  # Является ИПДЛ
                "mpdl": mpdl,  # Является МПДЛ
                "rpdl": rpdl  # Является РПДЛ
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

    def getCompanyManagement(self, supremeGoverningBody, selectedManagementKey):
        return {
            "companyManagement": {  # СТРУКТУРА ОРГАНОВ УПРАВЛЕНИЯ
                # Высший орган управления (выбор из справочника)
                "supremeGoverningBody": supremeGoverningBody,
                "selectedManagementKey": selectedManagementKey,
            }
        }

    def setTariff(self, tariff):
        self.json_api['selectedTariff'] = tariff

    def getLoadRequest_legalAddress(self):
        lr = self.loan_request
        addresses = lr.addresses
        for address in addresses:
            if "Юридический" in address['type_address']:
                return address['address']
        return ""

    def getLoadRequest_postalAddress(self):
        lr = self.loan_request
        addresses = lr.addresses
        for address in addresses:
            if "Почтовый" in address['type_address']:
                return address['address']
        return ""

    def parserCompanyPersons(self):
        companyPersons = []
        for persons in self.loan_request.list_persone:
            companyPersonsData = {}
            for key in persons:
                page = persons[key]
                companyPersonsData = {**companyPersonsData,  **page}
            companyPersons.append(companyPersonsData)
        return companyPersons

    def setCompany(self, company):
        self.json_api['company'] = company

    def setIsEioPDL(self, isEioPDL):
        self.json_api['isEioPDL'] = isEioPDL

    def setDocument(self, listObj):
        self.json_api['documents'] = listObj

    def getDocument(self, url, docType):
        response = session.get(os.getenv("DJANGO_APP_DOMAIN_STORAGE") + url)
        uri = (base64.b64encode(response.content).decode("utf-8"))
        nameFile = url.split('/')[-1]

        return {
            "docType": docType,  # Тип документа (справочник)
            "files": [
                {
                    "fileName": nameFile,
                    "content": uri
                }
            ]
        }

    def getCompanyBusinessInfo(self,
                               hasBeneficiariesInfo,
                               beneficiariesInfo,
                               companyCarriesOutActivitiesSubjectToLicensing,
                               historyReputationMarketSectorCompetition,
                               totalNumberOfTransactionsPerMonth,
                               totalNumberOfTransactionsPerWeek,
                               totalNumberOfTransactionsPerQuarter,
                               totalNumberOfTransactionsPerYear,
                               totalSumTransactionsPerMonth,
                               totalSumTransactionsPerWeek,
                               totalSumTransactionsPerQuarter,
                               totalSumTransactionsPerYear,
                               numberOfCashWithdrawalsPerMonth,
                               numberOfCashWithdrawalsPerWeek,
                               numberOfCashWithdrawalsPerQuarter,
                               numberOfCashWithdrawalsPerYear,
                               amountOfCashWithdrawalsPerMonth,
                               amountOfCashWithdrawalsPerWeek,
                               amountOfCashWithdrawalsPerQuarter,
                               amountOfCashWithdrawalsPerYear,
                               numberTransactionsOnForeignTradeContractsPerMonth,
                               numberTransactionsOnForeignTradeContractsPerWeek,
                               numberTransactionsOnForeignTradeContractsPerQuarter,
                               numberTransactionsOnForeignTradeContractsPerYear,
                               amountOfTransactionsUnderForeignTradeContractsPerMonth,
                               amountOfTransactionsUnderForeignTradeContractsPerWeek,
                               amountOfTransactionsUnderForeignTradeContractsPerQuarter,
                               amountOfTransactionsUnderForeignTradeContractsPerYear,
                               moneySources,
                               numberOfEmployees,
                               fatcaAndStrategicStatus,
                               ):
        return {
            "hasBeneficiariesInfo": hasBeneficiariesInfo,  # Сведения о выгодоприобретателях
            # Укажите третьи лица, к выгоде которых действует компания
            "beneficiariesInfo": beneficiariesInfo,
            # Компания осуществляет деятельность, подлежащую лицензированию (выбор из справочника)
            "companyCarriesOutActivitiesSubjectToLicensing": companyCarriesOutActivitiesSubjectToLicensing,
            # История, репутация, сектор рынка и конкуренция (выбор из справочника)
            "historyReputationMarketSectorCompetition": historyReputationMarketSectorCompetition,
            # Общее количество операций в месяц (выбор из справочника)
            "totalNumberOfTransactionsPerMonth": totalNumberOfTransactionsPerMonth,
            # Общее количество операций в неделю
            "totalNumberOfTransactionsPerWeek": totalNumberOfTransactionsPerWeek,
            # Общее количество операций в квартал
            "totalNumberOfTransactionsPerQuarter": totalNumberOfTransactionsPerQuarter,
            # Общее количество операций в год
            "totalNumberOfTransactionsPerYear": totalNumberOfTransactionsPerYear,
            # Общая сумма операций в месяц (выбор из справочника)
            "totalSumTransactionsPerMonth": totalSumTransactionsPerMonth,
            # Общая сумма операций в неделю
            "totalSumTransactionsPerWeek": totalSumTransactionsPerWeek,
            # Общая сумма операций в квартал
            "totalSumTransactionsPerQuarter": totalSumTransactionsPerQuarter,
            # Общая сумма операций в год
            "totalSumTransactionsPerYear": totalSumTransactionsPerYear,
            # Количество операций по снятию наличности в месяц (выбор из справочника)
            "numberOfCashWithdrawalsPerMonth": numberOfCashWithdrawalsPerMonth,
            # Количество операций по снятию наличности в неделю
            "numberOfCashWithdrawalsPerWeek": numberOfCashWithdrawalsPerWeek,
            # Количество операций по снятию наличности в квартал
            "numberOfCashWithdrawalsPerQuarter": numberOfCashWithdrawalsPerQuarter,
            # Количество операций по снятию наличности в год
            "numberOfCashWithdrawalsPerYear": numberOfCashWithdrawalsPerYear,
            # Сумма операций по снятию наличности в месяц (руб.) (выбор из справочника)
            "amountOfCashWithdrawalsPerMonth": amountOfCashWithdrawalsPerMonth,
            # Сумма операций по снятию денежных средств в наличной форме в неделю
            "amountOfCashWithdrawalsPerWeek": amountOfCashWithdrawalsPerWeek,
            # Сумма операций по снятию денежных средств в наличной форме в квартал
            "amountOfCashWithdrawalsPerQuarter": amountOfCashWithdrawalsPerQuarter,
            # Сумма операций по снятию денежных средств в наличной форме в год
            "amountOfCashWithdrawalsPerYear": amountOfCashWithdrawalsPerYear,
            # Количество операций по внешнеторговым контрактам в месяц (выбор из справочника)
            "numberTransactionsOnForeignTradeContractsPerMonth": numberTransactionsOnForeignTradeContractsPerMonth,
            # Количество операций по внешнеторговым контрактам в неделю
            "numberTransactionsOnForeignTradeContractsPerWeek": numberTransactionsOnForeignTradeContractsPerWeek,
            # Количество операций по внешнеторговым контрактам в квартал
            "numberTransactionsOnForeignTradeContractsPerQuarter": numberTransactionsOnForeignTradeContractsPerQuarter,
            # Количество операций по внешнеторговым контрактам в год
            "numberTransactionsOnForeignTradeContractsPerYear": numberTransactionsOnForeignTradeContractsPerYear,
            # Сумма операций по внешнеторговым контрактам в месяц (руб.) (выбор из справочника)
            "amountOfTransactionsUnderForeignTradeContractsPerMonth": amountOfTransactionsUnderForeignTradeContractsPerMonth,
            # Сумма операций по внешнеторговым контрактам в неделю
            "amountOfTransactionsUnderForeignTradeContractsPerWeek": amountOfTransactionsUnderForeignTradeContractsPerWeek,
            # Сумма операций по внешнеторговым контрактам в квартал
            "amountOfTransactionsUnderForeignTradeContractsPerQuarter": amountOfTransactionsUnderForeignTradeContractsPerQuarter,
            # Сумма операций по внешнеторговым контрактам в год
            "amountOfTransactionsUnderForeignTradeContractsPerYear": amountOfTransactionsUnderForeignTradeContractsPerYear,
            # Источники происхождения денежных средств (выбор из справочника)
            "moneySources": moneySources,
            # Штатная численность сотрудников (выбор из справочника)
            "numberOfEmployees": numberOfEmployees,
            # Отметьте все верные утверждения (множественный выбор из справочника)
            "fatcaAndStrategicStatus": fatcaAndStrategicStatus

        }

    def setInfoOnPurposesOfFinancialAndEconomicActivities(
        self,
        hasConstantPayers,
        hasConstantPayersDetails,
        hasConstantRecipient,
        hasConstantRecipientDetails
    ):
        if hasConstantPayers:
            self.json_api['infoOnPurposesOfFinancialAndEconomicActivities']['hasConstantPayers'] = hasConstantPayers
            self.json_api['infoOnPurposesOfFinancialAndEconomicActivities']['hasConstantPayersDetails'] = hasConstantPayersDetails
        else:
            self.json_api['infoOnPurposesOfFinancialAndEconomicActivities']['hasConstantPayers'] = hasConstantPayers
            self.json_api['infoOnPurposesOfFinancialAndEconomicActivities']['hasConstantPayersDetails'] = ""

        if hasConstantRecipient:
            self.json_api['infoOnPurposesOfFinancialAndEconomicActivities']['hasConstantRecipient'] = hasConstantRecipient
            self.json_api['infoOnPurposesOfFinancialAndEconomicActivities']['hasConstantRecipientDetails'] = hasConstantRecipientDetails
        else:
            self.json_api['infoOnPurposesOfFinancialAndEconomicActivities']['hasConstantRecipient'] = hasConstantRecipient
            self.json_api['infoOnPurposesOfFinancialAndEconomicActivities']['hasConstantRecipientDetails'] = ""

    def setCompanyBusinessInfo(self, obj):
        self.json_api['companyBusinessInfo'] = obj

    def setAdditionalProducts(
        self,
        sms,
        overdraft,
        internetAcquiring,
        merchantAcquiring,
        fastPaymentSystem,
        loyaltyProgram,
        loyaltyProgramInfo,
        community,
        accounting,
        legalSupport,
        promotion,
    ):
        self.json_api['additionalProducts'] = {
            "sms": sms,  # СМС-оповещение
            "overdraft": overdraft,  # Овердрафт
            "internetAcquiring": internetAcquiring,  # Интернет-эквайринг
            "merchantAcquiring": merchantAcquiring,  # Торговый эквайринг
            "fastPaymentSystem": fastPaymentSystem,  # Расчеты по Системе быстрых платежей
            "loyaltyProgram": loyaltyProgram,  # Подключить к Программе лояльности
            # Программа лояльности (выбор из справочника)
            "loyaltyProgramInfo": loyaltyProgramInfo,
            "community": community,  # Комьюнити
            "accounting": accounting,  # Бухгалтерия
            "legalSupport": legalSupport,  # Юридическая поддержка
            "promotion": promotion  # Продвижение
        }

    def setCodeword(self, codeword=""):
        self.json_api['codeword'] = codeword

    def getResult(self):
        lr = self.loan_request
        initiatorData = self.getInitiatorData(phoneNumber=lr.contact_number)
        self.setInitiator(initiator=initiatorData)

        legalAddress = self.getLoadRequest_legalAddress()
        postalAddress = self.getLoadRequest_postalAddress()

        companyBase = self.getCompanyBase(
            inn=lr.inn,
            ogrn=lr.ogrn,
            shortName=lr.short,
            shortNameEn="",
            legalAddress=legalAddress,
            postalAddress=postalAddress,
        )
        companyContacts = self.getCompanyContacts(
            email=lr.email,
            phone=lr.contact_number,
            webSite=lr.donainname,
            fax=lr.fax,
        )
        arrayCompanyFoundersUl = []

        if lr.founders:
            for item in lr.founders:
                arrayCompanyFoundersUl.append(CompanyFoundersUl(
                    inn=item['inn'],
                    share=item['share'],
                    ogrn=item['ogrn'],
                ))

        companyFoundersUl = self.getCompanyFoundersUl(arrayCompanyFoundersUl)

        lr_list_companyPersons = self.parserCompanyPersons()
        companyPersonsList = []

        for lr_persons in lr_list_companyPersons:
            print(lr_persons)
            companyPersonsBase = self.getCompanyPersonsBase(
                inn=lr_persons['account_onw_inn'],
                lastName=lr_persons['account_own_name'],
                firstName=lr_persons['account_own_lastname'],
                middleName=lr_persons['account_own_surname'],
                gender=(
                    1 if lr_persons['account_own_gender'] == 'Мужской' else 0
                ),
                birthDate=lr_persons['account_datebirth'],
                birthPlace=lr_persons['account_birth_place'],
                citizenship=lr_persons['account_own_citizenship'],
                countryOfResidence=lr_persons['account_country_residence'],
                registrationAddress=lr_persons['assigned_publ_pers_registraion'],
                actualAddress=lr_persons['accownt_own_living'],
            )

            companyContact = self.getContacts(
                phone=lr_persons['account_own_phone'],
                email=lr_persons['account_own_email'],
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
                companyHeadPosition=lr_persons['account_own_job_title'],
                founderShare=lr_persons['account_own_piece_auctioner'] if "account_own_piece_auctioner" in lr_persons else 0,
                beneficiaryShare=lr_persons['account_own_piece_beneficiary'] if "account_own_piece_beneficiary" in lr_persons else 0,
            )

            pdl = self.getPdl(
                ipdl=True,
                mpdl=True,
                rpdl=True,
            )

            companyPersons = self.getCompanyPersons(
                companyPersonsBase=companyPersonsBase,
                identityDocument=identityDocument,
                contacts=companyContact,
                roles=roles,
                pdl=pdl,
            )

            companyPersonsList.append(companyPersons)

        companyManagement = self.getCompanyManagement(
            supremeGoverningBody=lr.structure_value,
            selectedManagementKey=lr.structure_value,
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
        self.setCompanyBusinessInfo(
            self.getCompanyBusinessInfo(
                hasBeneficiariesInfo=lr.beneficiaries == 'Имеются',
                beneficiariesInfo=lr.third_parties,
                companyCarriesOutActivitiesSubjectToLicensing=lr.subject_licensing,
                historyReputationMarketSectorCompetition=lr.history_reputation,
                totalNumberOfTransactionsPerMonth=lr.num_transactions_month,
                totalNumberOfTransactionsPerWeek=lr.num_transactions_week,
                totalNumberOfTransactionsPerQuarter=lr.num_transactions_quarter,
                totalNumberOfTransactionsPerYear=lr.num_transactions_age,
                totalSumTransactionsPerMonth=lr.sum_transactions_month,
                totalSumTransactionsPerWeek=lr.sum_transactions_week,
                totalSumTransactionsPerQuarter=lr.sum_transactions_quarter,
                totalSumTransactionsPerYear=lr.sum_transactions_age,

                numberOfCashWithdrawalsPerMonth=lr.monthly_cash_withdrawal,
                numberOfCashWithdrawalsPerWeek=lr.week_cash_withdrawal,
                numberOfCashWithdrawalsPerQuarter=lr.quarter_cash_withdrawal,
                numberOfCashWithdrawalsPerYear=lr.age_cash_withdrawal,

                amountOfCashWithdrawalsPerMonth=lr.sum_mouth_cash_withdrawal,
                amountOfCashWithdrawalsPerWeek=lr.sum_week_cash_withdrawal,
                amountOfCashWithdrawalsPerQuarter=lr.sum_quarter_cash_withdrawal,
                amountOfCashWithdrawalsPerYear=lr.sum_age_cash_withdrawal,

                numberTransactionsOnForeignTradeContractsPerMonth=lr.foreign_trade_contracts_month,
                numberTransactionsOnForeignTradeContractsPerWeek=lr.foreign_trade_contracts_week,
                numberTransactionsOnForeignTradeContractsPerQuarter=lr.foreign_trade_contracts_quarter,
                numberTransactionsOnForeignTradeContractsPerYear=lr.foreign_trade_contracts_age,

                amountOfTransactionsUnderForeignTradeContractsPerMonth=lr.foreign_sum_contracts_month,
                amountOfTransactionsUnderForeignTradeContractsPerWeek=lr.foreign_sum_contracts_week,
                amountOfTransactionsUnderForeignTradeContractsPerQuarter=lr.foreign_sum_contracts_quarter,
                amountOfTransactionsUnderForeignTradeContractsPerYear=lr.foreign_sum_contracts_age,

                moneySources=lr.sources_cash_receipts,
                numberOfEmployees=lr.headcount,
                fatcaAndStrategicStatus=",".join(lr.information_goals),
            )
        )

        self.setIsEioPDL(lr.additional_inforamtion)

        self.setAdditionalProducts(
            sms='СМС-оповещение' in lr.additional_products,
            overdraft=False,
            internetAcquiring=False,
            merchantAcquiring=False,
            fastPaymentSystem=False,
            loyaltyProgram=False,
            loyaltyProgramInfo="first",
            community='Сообщество предпринимателей' in lr.additional_products,
            accounting='Онлайн-бухгалтерия' in lr.additional_products,
            legalSupport='Юридическая поддержка' in lr.additional_products,
            promotion='Привлечение клиентов' in lr.additional_products,
        )

        self.setCodeword(lr.codeword)

        self.setTariff(
            lr.tariff
        )

        self.setInfoOnPurposesOfFinancialAndEconomicActivities(
            hasConstantPayers=lr.hasConstantPayers == 'Да',
            hasConstantPayersDetails=lr.hasConstantPayersDetails,
            hasConstantRecipient=lr.hasConstantRecipient == 'Да',
            hasConstantRecipientDetails=lr.hasConstantRecipientDetails,
        )

        self.setTypesOfContracts(
            contractProvisionServices='Договор возмездного оказания услуг' in lr.planned_operations,
            supplyContract='Договор поставки' in lr.planned_operations,
            workAgreement='Договор подряда' in lr.planned_operations,
            commissionAgreement='Договор комиссии' in lr.planned_operations,
            contractOfSale='Договор купли-продажи' in lr.planned_operations,
            leaseAgreementForMovableProperty='Договор аренды движимого имущества' in lr.planned_operations,
            realEstateLeaseAgreement='Договор аренды недвижимого имущества' in lr.planned_operations,
            leasingAgreement='Договор лизинга' in lr.planned_operations,
            factoringAgreement='Договор факторинга' in lr.planned_operations,
            other='Иное (укажите)' in lr.planned_operations,
            contractsInfo=lr.planned_other,
        )

        documentList = []

        for image in lr.document_certifying_identity_executive:
            im = self.getDocument(url=image['path'], docType="executiveBody")
            documentList.append(im)

        for image in lr.document_confirming_real_activity:
            im = self.getDocument(
                url=image['path'], docType="additionalClientDocs")
            documentList.append(im)

        for image in lr.document_licenses:
            im = self.getDocument(url=image['path'], docType="license")
            documentList.append(im)

        for image in lr.document_certifying_identity_ceo:
            im = self.getDocument(url=image['path'], docType="dulHead")
            documentList.append(im)

        self.setDocument(documentList)

        return self.json_api
