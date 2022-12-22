export const translateMixin = {
    methods: {
        isTitle(name) {
            switch (name) {
                case 'account_birth_place': return 'Место рождения'
                case 'foreigner_doc_number': return 'Номер документа удостоверяющего личность'
                case 'is_person_a_foreign_public': return `Является ли лицо иностранным публичным должностным лицом либо лицом, связанным с таковым родственными
                партнерскими или иными отношениями?`
                case 'first_passport_page': return 'Паспорт'
                case "tariff":
                    return "Тариф";
                case "account_datebirth":
                    return "Дата рождения";
                case "account_onw_inn":
                    return "ИНН";
                case "account_onw_role":
                    return "Роль";
                case "account_own_citizenship":
                    return "Гражданство";
                case "account_own_firstname":
                    return "Имя";
                case "account_own_lastname":
                    return "Фамилия";
                case "account_own_surname":
                    return "Отчество";
                case "account_own_mail":
                    return "Адрес фактического проживания";
                case "account_own_name":
                    return "Пол";
                case "account_own_phone":
                    return "Телефон";
                case "account_own_piece":
                    return "Доля владения";
                case "operation_nalition":
                    return "Количество операций по снятию наличности в месяц";
                case "account_own_registration":
                    return "Адрес регистрации";
                case "account_own_snils":
                    return "СНИЛС";
                case "account_operations":
                    return "Расчетно-кассовое обслуживание";
                case "accownt_own_living":
                    return "Адрес проживания";
                case "assigned_publ_pers_registraion":
                    return "Адрес регистрации";
                case "assigned_publ_pers_relation":
                    return "Степень родства либо статус (супруг или супруга) по отношению к публичному должностному лицу";
                case "beneficiaries":
                    return "Выгодоприобретатели";
                case "cash_source":
                    return "Источники происхождения денежных средств";
                case "collegiate_body":
                    return "Наименование наблюдательного совета";
                case "collegiate_person":
                    return "Наименование коллегиального исполнительног органа";
                case "company_group_name":
                    return "Наименование группы компаний";
                case "company_name":
                    return "Наименование группы компаний";
                case "salary_debt":
                    return "Задолженность по зп";
                case "state_employers":
                    return "Штатная численость сотрудников";
                case "sum_per_month":
                    return "Сумма по снятию за месяц";
                case "date_issue":
                    return "Дата выдачи";
                case "division_code":
                    return "Код подразделения";
                case "employers_volume":
                    return "Численность персонала";
                case "end_date":
                    return "Дата окончания действия";
                case "groupList":
                    return "Список групп";
                case "group_members":
                    return "Состав группы компаний";
                case "issued_by":
                    return "Кем выдан";
                case "legal_address":
                    return "Юридический адрес";
                case "mail_address":
                    return "Почтовый адрес";
                case "outside_contracts_volume":
                    return "Количество операций по безлимитным платежам в месяц";
                case "passport_serial":
                    return "Серия паспорта";
                case "physic_address":
                    return "Физический адрес";
                case "placeOfBirth":
                    return "Место рождения";
                case "operation_volume":
                    return "Количество операций по безлимитным платежам в месяц";
                case "planned_operations":
                    return "Сведения о планируемых опреациях по счету";
                case "start_date":
                    return "Дата начала действия";
                case "supreme_management_body":
                    return "Высший орган управления";
                case "supervisoty_board_persone_name":
                    return "Наименование коллегиального исполнительного органа";
                case "is_supervisoty":
                    return "Наличие коллегиального исполнительного органа";
                case "supreme_management_inn":
                    return "ИНН";
                case "supreme_management_type":
                    return "Роль";
                case "validity":
                    return "Срок действия";
                case "contact_number":
                    return "Номер телефона";
                case "inn":
                    return "ИНН";
                case "addresses":
                    return "Адреса:";
                case "supreme_management_person":
                    return "Тип руководителя";
                case "collegiate_person_fio":
                    return "Члены коллегиального исполнительного органа";
                case "account_own_gender":
                    return "Пол";
                case "doc_number":
                    return "Номер документа удостоверяющего личность";
                case "doc_serial":
                    return "Серия документа удостоверяющего личность";
                case "doc_type":
                    return "Тип документа удостоверяющего личность";
                case "foreigner_doc_type":
                    return "Тип документа";
                case "foreigner_doc_serial":
                    return "Серия (если имеется)";
                case "foreigner_doc_issued":
                    return "Дата начала срока действия права пребывания(проживания)";
                case "foreigner_doc_validity":
                    return "Дата окончания срока действия права пребывания(проживания)";
                case "licenced_activity":
                    return "Перечень видов лицензируемой деятельности";
                case "typeAdress":
                    return "Тип Адреса";
                case "basis":
                    return "Основание";
                case "address":
                    return "Адрес";
                case "name":
                    return "Наименование";
                case "ogrn":
                    return "ОГРН";
                case "supervisory":
                    return "Наименование наблюдательного совета";
                case "is_collegiate_body":
                    return "Наличие наблюдательного совета";
                case "operation_sum":
                    return "Сумма операций по безналичным платежам в месяц";
                case "list_collegial_executive_body":
                    return "Члены коллегиального исполнительного органа";
                case "list_supervisoty_board_persone":
                    return "Члены наблюдательного совета";
                case "informationGoals":
                    return "Юридические лица компании";
                default: return name
            }
        },
    }
}