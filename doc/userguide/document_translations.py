from pathlib import Path

from robot.api import Language


class LanguageWrapper:

    def __init__(self, lang):
        self.lang = lang

    def __getattr__(self, name):
        return getattr(self.lang, name) or ''

    @property
    def underline(self):
        width = len(self.lang.name + self.lang.code) + 3
        return '-' * width

    @property
    def given_prefix(self):
        return ', '.join(self.lang.given_prefix)

    @property
    def when_prefix(self):
        return ', '.join(self.lang.when_prefix)

    @property
    def then_prefix(self):
        return ', '.join(self.lang.then_prefix)

    @property
    def and_prefix(self):
        return ', '.join(self.lang.and_prefix)

    @property
    def but_prefix(self):
        return ', '.join(self.lang.but_prefix)

    @property
    def true_strings(self):
        return ', '.join(self.lang.true_strings)

    @property
    def false_strings(self):
        return ', '.join(self.lang.false_strings)


TEMPLATE = '''
{lang.name} ({lang.code})
{lang.underline}

Section headers
~~~~~~~~~~~~~~~

.. list-table::
    :width: 40em
    :widths: 2 3
    :header-rows: 1
    
    * - Header
      - Translation
    * - Settings
      - {lang.settings_header}
    * - Variables
      - {lang.variables_header}
    * - Test Cases
      - {lang.test_cases_header}
    * - Tasks
      - {lang.tasks_header}
    * - Keywords
      - {lang.keywords_header}
    * - Comments
      - {lang.comments_header}
    
Settings
~~~~~~~~

.. list-table::
    :width: 40em
    :widths: 2 3
    :header-rows: 1
    
    * - Setting
      - Translation
    * - Library
      - {lang.library_setting}
    * - Resource
      - {lang.resource_setting}
    * - Variables
      - {lang.variables_setting}
    * - Documentation
      - {lang.documentation_setting}
    * - Metadata
      - {lang.metadata_setting}
    * - Suite Setup
      - {lang.suite_setup_setting}
    * - Suite Teardown
      - {lang.suite_teardown_setting}
    * - Test Setup
      - {lang.test_setup_setting}
    * - Task Setup
      - {lang.task_setup_setting}
    * - Test Teardown
      - {lang.test_teardown_setting}
    * - Task Teardown
      - {lang.task_teardown_setting}
    * - Test Template
      - {lang.test_template_setting}
    * - Task Template
      - {lang.task_template_setting}
    * - Test Timeout
      - {lang.test_timeout_setting}
    * - Task Timeout
      - {lang.task_timeout_setting}
    * - Test Tags
      - {lang.test_tags_setting}
    * - Task Tags
      - {lang.task_tags_setting}
    * - Keyword Tags
      - {lang.keyword_tags_setting}
    * - Tags
      - {lang.tags_setting}
    * - Setup
      - {lang.setup_setting}
    * - Teardown
      - {lang.teardown_setting}
    * - Template
      - {lang.template_setting}
    * - Timeout
      - {lang.timeout_setting}
    * - Arguments
      - {lang.arguments_setting}

BDD prefixes
~~~~~~~~~~~~

.. list-table::
    :width: 40em
    :widths: 2 3
    :header-rows: 1
    
    * - Prefix
      - Translation
    * - Given
      - {lang.given_prefix}
    * - When
      - {lang.when_prefix}
    * - Then
      - {lang.then_prefix}
    * - And
      - {lang.and_prefix}
    * - But
      - {lang.but_prefix}

Boolean strings
~~~~~~~~~~~~~~~

.. list-table::
    :width: 40em
    :widths: 2 3
    :header-rows: 1
    
    * - True/False
      - Values
    * - True
      - {lang.true_strings}
    * - False
      - {lang.false_strings}
'''


def document_translations(file):
    languages = [lang for lang in Language.__subclasses__() if lang.code != 'en']
    for index, lang in enumerate(sorted(languages, key=lambda lang: lang.code)):
        file.write(TEMPLATE.format(lang=LanguageWrapper(lang)))
        if index < len(languages) - 1:
            file.write('\n\n')


if __name__ == '__main__':
    target = Path(__file__).absolute().parent / 'src/Appendices/Translations.rst'
    source = target.read_text(encoding='UTF-8')
    with open(target, 'w', encoding='UTF-8') as file:
        for line in source.splitlines(keepends=True):
            file.write(line)
            if line == '.. GENERATED CONTENT BEGINS\n':
                break
        document_translations(file)
