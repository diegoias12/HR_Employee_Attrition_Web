$(document).ready(function () {
    $('#valEnvSat').html($('#intEnvSat').val());
    $('#intEnvSat').on('input', function(){
        $('#valEnvSat').html($(this).val());
    });

    $('#valJobInv').html($('#intJobInv').val());
    $('#intJobInv').on('input', function(){
        $('#valJobInv').html($(this).val());
    });

    $('#valJobLev').html($('#intJobLev').val());
    $('#intJobLev').on('input', function(){
        $('#valJobLev').html($(this).val());
    });

    $('#valStoLev').html($('#intStoLev').val());
    $('#intStoLev').on('input', function(){
        $('#valStoLev').html($(this).val());
    });
});
