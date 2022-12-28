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
                case "information_goals":
                    return "Сведения о бизнесе";
                case "account_own_citizenship":
                    return "Гражданство";
                case "account_own_email":
                    return "Эл. почта";
                case "account_own_job_title":
                    return "Должность";
                case "is_accownt_own_living":
                    return "Адрес фактического проживания совпадает";
                case "codeword":
                    return "Кодовое слово";
                case "founders":
                    return "Учредители - юридические лица";
                case "founder_inn":
                    return "Учередитель ИНН";
                case "founder_name":
                    return "Учередитель наименование";
                case "capital":
                    return "Доля в уставном капитале";
                case "structure_value":
                    return "Доля в уставном капитале";
                case "is_conditions":
                    return "Согласен с условиями";
                case "contact_phone_number":
                    return "Номер телефона";
                case "donainname":
                    return "Доменное имя";
                case "fax":
                    return "Факс";
                case "list_persone":
                    return "Физические лица";
                case "additional_products":
                    return "Дополнительные продукты";
                case "email":
                    return "Электронная почта";
                case "subject_licensing":
                    return "Компания осуществляет деятельность, подлежащую лицензированию";
                case "history_reputation":
                    return "История, репутация, сектор рынка и конкуренция";
                case "num_transactions_month":
                    return "Общее количество операций в месяц";
                case "num_transactions_week":
                    return "Общее количество операций в неделю";
                case "num_transactions_quarter":
                    return "Общее количество операций в квартал";
                case "num_transactions_age":
                    return "Общее количество операций в год";
                case "sum_transactions_month":
                    return "Общая сумма операций в месяц";
                case "sum_transactions_week":
                    return "Общая сумма операций в неделю";
                case "sum_transactions_quarter":
                    return "Общая сумма операций в квартал";
                case "sum_transactions_age":
                    return "Общая сумма операций в год";
                case "monthly_cash_withdrawal":
                    return "Количество операций по снятию наличности в месяц";
                case "week_cash_withdrawal":
                    return "Количество операций по снятию наличности в неделю";
                case "quarter_cash_withdrawal":
                    return "Количество операций по снятию наличности в квартал";
                case "age_cash_withdrawal":
                    return "Количество операций по снятию наличности в год";
                case "sum_mouth_cash_withdrawal":
                    return "Сумма операций по снятию наличности в месяц";
                case "sum_week_cash_withdrawal":
                    return "Сумма операций по снятию денежных средств в наличной форме в неделю";
                case "sum_quarter_cash_withdrawal":
                    return "Сумма операций по снятию денежных средств в наличной форме в квартал";
                case "sum_age_cash_withdrawal":
                    return "Сумма операций по снятию денежных средств в наличной форме в год";
                case "foreign_trade_contracts_month":
                    return "Количество операций по внешнеторговым контрактам в месяц";
                case "foreign_trade_contracts_week":
                    return "Количество операций по внешнеторговым контрактам в неделю";
                case "foreign_trade_contracts_quarter":
                    return "Количество операций по внешнеторговым контрактам в квартал";
                case "foreign_trade_contracts_age":
                    return "Количество операций по внешнеторговым контрактам в год";
                case "foreign_sum_contracts_month":
                    return "Сумма операций по внешнеторговым контрактам в месяц";
                case "foreign_sum_contracts_week":
                    return "Сумма операций по внешнеторговым контрактам в неделю";
                case "foreign_sum_contracts_quarter":
                    return "Сумма операций по внешнеторговым контрактам в квартал";
                case "foreign_sum_contracts_age":
                    return "Сумма операций по внешнеторговым контрактам в год";
                case "sources_cash_receipts":
                    return "Источники поступления денежных средств";
                case "headcount":
                    return "Штатная численность сотрудников";


                default: return name
            }
        },

        translateValue(name) {
            switch (name) {
                case "isFatcaFinanceInstitute":
                    return "Является ли юридическое лицо Финансовым институтом в соответствии с Законом США «О налогообложении иностранных счетов» (FATCA) и/или главой 20.1 Налогового кодекса РФ";
                case "isForeignTaxResident":
                    return "Является ли юридическое лицо, или бенефициар, или выгодоприобретатель налоговым резидентом иностранного государства и/или у юридического лица, бенефициара или выгодоприобретателя отсутствует налоговое резидентство во всех государствах (территориях))? Имеет ли юридическое лицо признаки Пассивной нефинансовой организации";
                case "isForeignTaxResidentIndividual":
                    return "Подтверждаю и гарантирую, что все Выгодоприобретатели/бенефициары индивидуального предпринимателя являются налогоплательщиками исключительно в РФ и, если выгодоприобретателем является юридическое лицо, то оно не имеет признаков Пассивной нефинансовой организации";
                case "isUsaTaxResident":
                    return "Является ли юридическое лицо, выгодоприобретатель или бенефициар налоговым резидентом США?";
                case "isStrategicImportanceOPK":
                    return "Компания осуществляет виды деятельности, которые могут иметь стратегическое значение для оборонно-промышленного комплекса и безопасности РФ";
                case "isStrategicImportanceOPK213FZ":
                    return "Компания является хозяйственным обществом, имеющим стратегическое значение для оборонно-промышленного комплекса и безопасности РФ либо обществом, находящимся под его прямым или косвенным контролем, которые указаны в Федеральном законе от 21.07.2014 № 213-ФЗ";
                case "isNoneOfThis":
                    return "Компания не относится к указанным в настоящем пункте юридическим лицам";
                case "from-10":
                    return "От 10";
                case "from-100":
                    return "От 100";
                case "from-1000":
                    return "От 1000";
                case "to-1-mln":
                    return "До 1 000 000";
                case "to-10-mln":
                    return "До 10 000 000";
                case "to-100-mln":
                    return "До 100 000 000";
                case "more-100-mln":
                    return "Свыше 100 000 000";
                case "founderFunding":
                    return "Финансирование учредителей/участников";
                case "incomeFromMainActivity":
                    return "Доходы от основного вида деятельности";
                case "incomeFromAdditionalActivity":
                    return "Доходы от дополнительных видов деятельности";
                case "borrowed":
                    return "Заемные (кредитные)/привлеченные денежные средства";
                case "governmentFunding":
                    return "Государственное финансирование";
                case "other":
                    return "Иное";
                case "first":
                    return "Первый";
                case "second":
                    return "Второй";
                case "third":
                    return "Третий";


                default: return name;
            }
        }
    }
}