// chart.js script to populate the user dashboard with statistics
$(function () {

    // 'all_features_chart' is the ID of the canvas element, which in turn is calling the feature_chart view
    var $allFeaturesChart = $("#all_features_chart");
    $.ajax({
        url: $allFeaturesChart.data("url"),
        success: function (data) {

            var ctx = $allFeaturesChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Feature',
                        backgroundColor: '#56CC9D',
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'All Active Features'
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            },
                            scaleLabel: {
                                display: true,
                                labelString: 'Total Contributions'
                            }
                        }]
                    }
                }
            });

        }
    });

    // 'my_features_chart' filters all features contributed to by the requesting user
    var $myFeaturesChart = $("#my_features_chart");
    $.ajax({
        url: $myFeaturesChart.data("url"),
        success: function (data) {

            var ctx = $myFeaturesChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Feature',
                        backgroundColor: '#F3969A',
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Features I Have Contributed To'
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            },
                            scaleLabel: {
                                display: true,
                                labelString: 'Total Contributions'
                            }
                        }]
                    }
                }
            });

        }
    });

    // 'my_bugs_chart' filters based on the the bugs which have been voted on by the requesting user
    var $myVotedBugsChart = $("#my_voted_bugs_chart");
    $.ajax({
        url: $myVotedBugsChart.data("url"),
        success: function (data) {

            var ctx = $myVotedBugsChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Bug',
                        backgroundColor: '#F3969A',
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Bugs I have Voted On'
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            },
                            scaleLabel: {
                                display: true,
                                labelString: 'Total Votes'
                            }
                        }]
                    }
                }
            });

        }
    });

    // 'all_bugs_chart' is the ID of the canvas element, which in turn is calling the all_bugs_chart view
    var $allBugsChart = $("#all_bugs_chart");
    $.ajax({
        url: $allBugsChart.data("url"),
        success: function (data) {

            var ctx = $allBugsChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Bug',
                        backgroundColor: '#F3969A',
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'All Active Bugs'
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            },
                            scaleLabel: {
                                display: true,
                                labelString: 'Total Votes'
                            }
                        }]
                    }
                }
            });

        }
    });


    // 'resolved_bugs_chart' is the ID of the canvas element, which in turn is calling the all_bugs_chart view
    // This creates a graph showing the latest resolved bugs and their time to resolution
    var $resolvedBugsChart = $("#resolved_bugs_chart");
    $.ajax({
        url: $resolvedBugsChart.data("url"),
        success: function (data) {

            var ctx = $resolvedBugsChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Bug',
                        backgroundColor: '#F3969A',
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Resolved Bugs'
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            },
                            scaleLabel: {
                                display: true,
                                labelString: 'Days to Resolution'
                            }
                        }]
                    }
                }
            });
        }
    });
});