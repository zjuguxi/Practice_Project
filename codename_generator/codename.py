import pypdftk

datas = {
    'WORD1': 'Julien',
    'WORD2': 'revolunet',
    'WORD3': 42
}
generated_pdf = pypdftk.fill_form('./template.pdf', datas)
out_pdf = pypdftk.concat(['./new.pdf', generated_pdf])