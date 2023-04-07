// Problem: 9. Palindrome Number


function isPalindrome(x) {
    const xString = x.toString();
    let left = 0;
    let right = xString.length - 1;
    while (left <= right) {
        if (xString[left] === xString[right]) {
            left += 1;
            right -= 1;
        } else {
            return false;
        }
    }
    return true;
}


answer = isPalindrome(121)
console.log(answer)

/*
Для решения данной задачи используется алгоритм 2 указателей, при котором используются левый (left) и правый (right)
указатели. В цикле while проверяется условие left <= right, что означает, что указатели ещё не встретились. Если данное
условие верно, то происходит проверка на равенство символов строки с индексом left и right. Если символы равны, то мы
сужаем указатели, увеличивая значение left на 1 и уменьшая значение right на 1. Если символы не равны, то функция
возвращает значение false. Если цикл while завершается без возврата false, то число является палиндромом, и функция
возвращает значение true.
*/