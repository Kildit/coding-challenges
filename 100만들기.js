/**
 * 1부터 7까지의 연속된 숫자들을 분할하여 4칙 연산(+, -, *, /)을 하였을 때,
 * 100이 되는 경우를 모두 찾아보시오.
 */

'use strict';

const LAST_NUMBER = 7;
const ANSWER = 100;


var n_list = new Array(),
    op_list = ['', '+', '-', '*', '/', '%'];

for (let i = 1; i <= LAST_NUMBER; i++) {
    n_list.push({
        op: '',
        num: i.toString()
    });
}

var count = 0;
(function cases(index) {
    if (index < n_list.length) {
        for (var i = 0; i < op_list.length; i++) {
            n_list[index].op = op_list[i];
            cases(index+1);
        }
    } else {
        let formula = (() => {
            let res = '';
            for (let i = 0; i < n_list.length; i++) {
                res += n_list[i].op + n_list[i].num;
            }
            return res;
        })();
        let value = eval(formula);
        if (value == ANSWER) {
            count++;
            console.log(count, formula);
        }
    }
})(1);
