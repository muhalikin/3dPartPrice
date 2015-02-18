'''OpenGL extension EXT.index_array_formats

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_index_array_formats'
_DEPRECATED = False
GL_IUI_V2F_EXT = constant.Constant( 'GL_IUI_V2F_EXT', 0x81AD )
GL_IUI_V3F_EXT = constant.Constant( 'GL_IUI_V3F_EXT', 0x81AE )
GL_IUI_N3F_V2F_EXT = constant.Constant( 'GL_IUI_N3F_V2F_EXT', 0x81AF )
GL_IUI_N3F_V3F_EXT = constant.Constant( 'GL_IUI_N3F_V3F_EXT', 0x81B0 )
GL_T2F_IUI_V2F_EXT = constant.Constant( 'GL_T2F_IUI_V2F_EXT', 0x81B1 )
GL_T2F_IUI_V3F_EXT = constant.Constant( 'GL_T2F_IUI_V3F_EXT', 0x81B2 )
GL_T2F_IUI_N3F_V2F_EXT = constant.Constant( 'GL_T2F_IUI_N3F_V2F_EXT', 0x81B3 )
GL_T2F_IUI_N3F_V3F_EXT = constant.Constant( 'GL_T2F_IUI_N3F_V3F_EXT', 0x81B4 )


def glInitIndexArrayFormatsEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
