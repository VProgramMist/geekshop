function number_format(number, decimals, dec_point, thousands_sep) {
    number = (number + '').replace(/[^0-9+\-Ee.]/g, '');
    var n = !isFinite(+number) ? 0 : +number,
        prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
        sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
        dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
        s = '',
        toFixedFix = function (n, prec) {
            var k = Math.pow(10, prec);
            return '' + (Math.round(n * k) / k)
                .toFixed(prec);
        };

    s = (prec ? toFixedFix(n, prec) : '' + Math.round(n))
        .split('.');
    if (s[0].length > 3) {
        s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
    }
    if ((s[1] || '')
        .length < prec) {
        s[1] = s[1] || '';
        s[1] += new Array(prec - s[1].length + 1)
            .join('0');
    }
    return s.join(dec);
}

$(document).ready(function () {
    let total_quantity = 0;
    $('.field-quantity').each(function () {
        total_quantity += Number(this.innerHTML);
    });

    let total_sum = 0.0;
    $('.field-sum').each(function () {
        total_sum += Number(this.innerHTML.replace(',', '.'));
    });

    let summary_row = '';
    let $trLast = $('#result_list > tbody tr:last-child'),
        $trNew = $trLast.clone();


    let cols = $trNew.find('td, th');

    $.each(cols, function () {
        if (this.localName === 'th')
            this.innerHTML = '<a href="#">ИТОГО</a>';
        else if (this.className === 'field-quantity')
            this.innerHTML = total_quantity;
        else if (this.className === 'field-sum')
            this.innerHTML = number_format(total_sum, 2, ',', '');
        else this.innerHTML = '';
    });

    $trNew[0].className = 'row2';
    $trLast.after($trNew);
});