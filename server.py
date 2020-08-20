from flask import Flask, request
import re
app = Flask(__name__)


SQL_INJECTION_REGEX_1 = re.compile(r'(=)|(<)|(>)|(\')|(--)|(\/)|(\+)|(;)|(\*)|(!)|({)|(})|(drop table)|(drop stored)|(alter table)|(alter stored)|(sp_)|(xp_)|(exec )|(execute )|(fetch)|(select)|(kill)|(selectsys)|(sysobjects)|(syscolumns)|(isnull)|(coalesce)|(dbo)|(tbl)|(usp)')
      
@app.route('/v1/sanitized/input/', methods=['POST'])

def test_input():
    response = {}
    
    #assigns payload value to variable called input

    input = request.json
    print("input:  ",input ['payload'])

    # if any match is found respond with {'result': 'unsanitized'}.  If no matches found respond with {'result': 'sanitized'}

    if SQL_INJECTION_REGEX_1.search(input ['payload']):
        response ['result'] = 'unsanitized'
    else:
        response ['result'] = 'sanitized'
    return response
    
if __name__ == "__main__":
    app.run(debug=True)