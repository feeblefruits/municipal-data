from django.http import Http404
from django.shortcuts import render
from cubes import cube_manager

from utils import jsonify, csvify


def get_cube(name):
    """ Load the named cube from the current registered ``CubeManager``. """
    if not cube_manager.has_cube(name):
        raise Http404('No such cube: %s' % name)
    return cube_manager.get_cube(name)


def explore(request, cube_name):
    return render(request, 'explore.html', {
        'cube_name': cube_name,
    })


def docs(request):
    cubes = []
    for cube_name in cube_manager.list_cubes():
        cubes.append({
            'model': cube_manager.get_cube(cube_name).model.to_dict(),
            'name': cube_name,
        })

    return render(request, 'docs.html', {
        'cubes': cubes,
    })


def status(request):
    """ General system status report :) """
    from babbage import __version__, __doc__
    return jsonify({
        'status': 'ok',
        'api': 'babbage',
        'message': __doc__,
        'version': __version__
    })


def cubes(request):
    """ Get a listing of all publicly available cubes. """
    cubes = []
    for cube in cube_manager.list_cubes():
        cubes.append({
            'name': cube
        })
    return jsonify({
        'status': 'ok',
        'data': cubes
    })


def model(request, cube_name):
    """ Get the model for the specified cube. """
    cube = get_cube(cube_name)
    cube.compute_cardinalities()
    return jsonify({
        'status': 'ok',
        'name': cube_name,
        'model': cube.model
    })


def aggregate(request, cube_name):
    """ Perform an aggregation request. """
    cube = get_cube(cube_name)
    result = cube.aggregate(aggregates=request.GET.get('aggregates'),
                            drilldowns=request.GET.get('drilldown'),
                            cuts=request.GET.get('cut'),
                            order=request.GET.get('order'),
                            page=request.GET.get('page'),
                            page_size=request.GET.get('pagesize'))

    format = request.GET.get('format', 'json')
    if format == 'json':
        result['status'] = 'ok'
        return jsonify(result)
    elif format == 'csv':
        fields = result['attributes'] + result['aggregates']
        return csvify(cube_name + '_aggregate', fields, result['cells'])


def facts(request, cube_name):
    """ List the fact table entries in the current cube. This is the full
    materialized dataset. """
    cube = get_cube(cube_name)
    result = cube.facts(fields=request.GET.get('fields'),
                        cuts=request.GET.get('cut'),
                        order=request.GET.get('order'),
                        page=request.GET.get('page'),
                        page_size=request.GET.get('pagesize'))

    format = request.GET.get('format', 'json')
    if format == 'json':
        result['status'] = 'ok'
        return jsonify(result)
    elif format == 'csv':
        return csvify(cube_name + '_facts', result['fields'], result['data'])


def members(request, cube_name, member_ref):
    """ List the members of a specific dimension or the distinct values of a
    given attribute. """
    cube = get_cube(cube_name)
    result = cube.members(member_ref,
                          cuts=request.GET.get('cut'),
                          order=request.GET.get('order'),
                          page=request.GET.get('page'),
                          page_size=request.GET.get('pagesize'))

    format = request.GET.get('format', 'json')
    if format == 'json':
        result['status'] = 'ok'
        return jsonify(result)
    elif format == 'csv':
        return csvify(cube_name + '_members', result['fields'], result['data'])
