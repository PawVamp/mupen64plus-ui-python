# -*- coding: utf-8 -*-
# Author: Milan Nikolic <gen2brain@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtCore import Qt

from m64py.frontend.keycodes import *

QT2SDL2 = {}
SCANCODE2KEYCODE = {}
KEYCODE2SCANCODE = {}

QT2SDL2[Qt.Key_A] = SDL_SCANCODE_A
QT2SDL2[Qt.Key_B] = SDL_SCANCODE_B
QT2SDL2[Qt.Key_C] = SDL_SCANCODE_C
QT2SDL2[Qt.Key_D] = SDL_SCANCODE_D
QT2SDL2[Qt.Key_E] = SDL_SCANCODE_E
QT2SDL2[Qt.Key_F] = SDL_SCANCODE_F
QT2SDL2[Qt.Key_G] = SDL_SCANCODE_G
QT2SDL2[Qt.Key_H] = SDL_SCANCODE_H
QT2SDL2[Qt.Key_I] = SDL_SCANCODE_I
QT2SDL2[Qt.Key_J] = SDL_SCANCODE_J
QT2SDL2[Qt.Key_K] = SDL_SCANCODE_K
QT2SDL2[Qt.Key_L] = SDL_SCANCODE_L
QT2SDL2[Qt.Key_M] = SDL_SCANCODE_M
QT2SDL2[Qt.Key_N] = SDL_SCANCODE_N
QT2SDL2[Qt.Key_O] = SDL_SCANCODE_O
QT2SDL2[Qt.Key_P] = SDL_SCANCODE_P
QT2SDL2[Qt.Key_Q] = SDL_SCANCODE_Q
QT2SDL2[Qt.Key_R] = SDL_SCANCODE_R
QT2SDL2[Qt.Key_S] = SDL_SCANCODE_S
QT2SDL2[Qt.Key_T] = SDL_SCANCODE_T
QT2SDL2[Qt.Key_U] = SDL_SCANCODE_U
QT2SDL2[Qt.Key_V] = SDL_SCANCODE_V
QT2SDL2[Qt.Key_W] = SDL_SCANCODE_W
QT2SDL2[Qt.Key_X] = SDL_SCANCODE_X
QT2SDL2[Qt.Key_Y] = SDL_SCANCODE_Y
QT2SDL2[Qt.Key_Z] = SDL_SCANCODE_Z
QT2SDL2[Qt.Key_0] = SDL_SCANCODE_0
QT2SDL2[Qt.Key_1] = SDL_SCANCODE_1
QT2SDL2[Qt.Key_2] = SDL_SCANCODE_2
QT2SDL2[Qt.Key_3] = SDL_SCANCODE_3
QT2SDL2[Qt.Key_4] = SDL_SCANCODE_4
QT2SDL2[Qt.Key_5] = SDL_SCANCODE_5
QT2SDL2[Qt.Key_6] = SDL_SCANCODE_6
QT2SDL2[Qt.Key_7] = SDL_SCANCODE_7
QT2SDL2[Qt.Key_8] = SDL_SCANCODE_8
QT2SDL2[Qt.Key_9] = SDL_SCANCODE_9
QT2SDL2[Qt.Key_F1] = SDL_SCANCODE_F1
QT2SDL2[Qt.Key_F2] = SDL_SCANCODE_F2
QT2SDL2[Qt.Key_F3] = SDL_SCANCODE_F3
QT2SDL2[Qt.Key_F4] = SDL_SCANCODE_F4
QT2SDL2[Qt.Key_F5] = SDL_SCANCODE_F5
QT2SDL2[Qt.Key_F6] = SDL_SCANCODE_F6
QT2SDL2[Qt.Key_F7] = SDL_SCANCODE_F7
QT2SDL2[Qt.Key_F8] = SDL_SCANCODE_F8
QT2SDL2[Qt.Key_F9] = SDL_SCANCODE_F9
QT2SDL2[Qt.Key_F10] = SDL_SCANCODE_F10
QT2SDL2[Qt.Key_F11] = SDL_SCANCODE_F11
QT2SDL2[Qt.Key_F12] = SDL_SCANCODE_F12
QT2SDL2[Qt.Key_F13] = SDL_SCANCODE_F13
QT2SDL2[Qt.Key_F14] = SDL_SCANCODE_F14
QT2SDL2[Qt.Key_F15] = SDL_SCANCODE_F15
QT2SDL2[Qt.Key_Insert] = SDL_SCANCODE_INSERT
QT2SDL2[Qt.Key_Delete] = SDL_SCANCODE_DELETE
QT2SDL2[Qt.Key_Home] = SDL_SCANCODE_HOME
QT2SDL2[Qt.Key_End] = SDL_SCANCODE_END
QT2SDL2[Qt.Key_PageUp] = SDL_SCANCODE_PAGEUP
QT2SDL2[Qt.Key_PageDown] = SDL_SCANCODE_PAGEDOWN
QT2SDL2[Qt.Key_Up] = SDL_SCANCODE_UP
QT2SDL2[Qt.Key_Down] = SDL_SCANCODE_DOWN
QT2SDL2[Qt.Key_Left] = SDL_SCANCODE_LEFT
QT2SDL2[Qt.Key_Right] = SDL_SCANCODE_RIGHT
QT2SDL2[Qt.Key_Return] = SDL_SCANCODE_RETURN
QT2SDL2[Qt.Key_Enter] = SDL_SCANCODE_RETURN2
QT2SDL2[Qt.Key_Escape] = SDL_SCANCODE_ESCAPE
QT2SDL2[Qt.Key_Pause] = SDL_SCANCODE_PAUSE
QT2SDL2[Qt.Key_QuoteLeft] = SDL_SCANCODE_GRAVE
QT2SDL2[Qt.Key_Backspace] = SDL_SCANCODE_BACKSPACE
QT2SDL2[Qt.Key_Tab] = SDL_SCANCODE_TAB
QT2SDL2[Qt.Key_CapsLock] = SDL_SCANCODE_CAPSLOCK
QT2SDL2[Qt.Key_Space] = SDL_SCANCODE_SPACE
QT2SDL2[Qt.Key_Slash] = SDL_SCANCODE_SLASH
QT2SDL2[Qt.Key_Backslash] = SDL_SCANCODE_BACKSLASH
QT2SDL2[Qt.Key_Minus] = SDL_SCANCODE_MINUS
QT2SDL2[Qt.Key_Plus] = SDL_SCANCODE_UNKNOWN
QT2SDL2[Qt.Key_Equal] = SDL_SCANCODE_EQUALS
QT2SDL2[Qt.Key_BracketLeft] = SDL_SCANCODE_LEFTBRACKET
QT2SDL2[Qt.Key_BracketRight] = SDL_SCANCODE_RIGHTBRACKET
QT2SDL2[Qt.Key_Semicolon] = SDL_SCANCODE_SEMICOLON
QT2SDL2[Qt.Key_Apostrophe] = SDL_SCANCODE_APOSTROPHE
QT2SDL2[Qt.Key_Comma] = SDL_SCANCODE_COMMA
QT2SDL2[Qt.Key_Period] = SDL_SCANCODE_PERIOD
QT2SDL2[Qt.Key_Alt] = SDL_SCANCODE_LALT
QT2SDL2[Qt.Key_Control] = SDL_SCANCODE_LCTRL
QT2SDL2[Qt.Key_Shift] = SDL_SCANCODE_LSHIFT
QT2SDL2[Qt.AltModifier.__int__()] = SDL_SCANCODE_LALT
QT2SDL2[Qt.ControlModifier.__int__()] = SDL_SCANCODE_LCTRL
QT2SDL2[Qt.ShiftModifier.__int__()] = SDL_SCANCODE_LSHIFT
QT2SDL2[Qt.Key_Print] = SDL_SCANCODE_PRINTSCREEN
QT2SDL2[Qt.Key_ScrollLock] = SDL_SCANCODE_SCROLLLOCK
QT2SDL2[Qt.Key_Meta] = SDL_SCANCODE_LGUI
QT2SDL2[Qt.MetaModifier.__int__()] = SDL_SCANCODE_LGUI
QT2SDL2[Qt.Key_Super_L] = SDL_SCANCODE_LGUI
QT2SDL2[Qt.Key_Super_R] = SDL_SCANCODE_RGUI
QT2SDL2[Qt.Key_unknown] = SDL_SCANCODE_UNKNOWN

SCANCODE2KEYCODE[SDL_SCANCODE_A] = SDLK_a
SCANCODE2KEYCODE[SDL_SCANCODE_B] = SDLK_b
SCANCODE2KEYCODE[SDL_SCANCODE_C] = SDLK_c
SCANCODE2KEYCODE[SDL_SCANCODE_D] = SDLK_d
SCANCODE2KEYCODE[SDL_SCANCODE_E] = SDLK_e
SCANCODE2KEYCODE[SDL_SCANCODE_F] = SDLK_f
SCANCODE2KEYCODE[SDL_SCANCODE_G] = SDLK_g
SCANCODE2KEYCODE[SDL_SCANCODE_H] = SDLK_h
SCANCODE2KEYCODE[SDL_SCANCODE_I] = SDLK_i
SCANCODE2KEYCODE[SDL_SCANCODE_J] = SDLK_j
SCANCODE2KEYCODE[SDL_SCANCODE_K] = SDLK_k
SCANCODE2KEYCODE[SDL_SCANCODE_L] = SDLK_l
SCANCODE2KEYCODE[SDL_SCANCODE_M] = SDLK_m
SCANCODE2KEYCODE[SDL_SCANCODE_N] = SDLK_n
SCANCODE2KEYCODE[SDL_SCANCODE_O] = SDLK_o
SCANCODE2KEYCODE[SDL_SCANCODE_P] = SDLK_p
SCANCODE2KEYCODE[SDL_SCANCODE_Q] = SDLK_q
SCANCODE2KEYCODE[SDL_SCANCODE_R] = SDLK_r
SCANCODE2KEYCODE[SDL_SCANCODE_S] = SDLK_s
SCANCODE2KEYCODE[SDL_SCANCODE_T] = SDLK_t
SCANCODE2KEYCODE[SDL_SCANCODE_U] = SDLK_u
SCANCODE2KEYCODE[SDL_SCANCODE_V] = SDLK_v
SCANCODE2KEYCODE[SDL_SCANCODE_W] = SDLK_w
SCANCODE2KEYCODE[SDL_SCANCODE_X] = SDLK_x
SCANCODE2KEYCODE[SDL_SCANCODE_Y] = SDLK_y
SCANCODE2KEYCODE[SDL_SCANCODE_Z] = SDLK_z
SCANCODE2KEYCODE[SDL_SCANCODE_0] = SDLK_0
SCANCODE2KEYCODE[SDL_SCANCODE_1] = SDLK_1
SCANCODE2KEYCODE[SDL_SCANCODE_2] = SDLK_2
SCANCODE2KEYCODE[SDL_SCANCODE_3] = SDLK_3
SCANCODE2KEYCODE[SDL_SCANCODE_4] = SDLK_4
SCANCODE2KEYCODE[SDL_SCANCODE_5] = SDLK_5
SCANCODE2KEYCODE[SDL_SCANCODE_6] = SDLK_6
SCANCODE2KEYCODE[SDL_SCANCODE_7] = SDLK_7
SCANCODE2KEYCODE[SDL_SCANCODE_8] = SDLK_8
SCANCODE2KEYCODE[SDL_SCANCODE_9] = SDLK_9
SCANCODE2KEYCODE[SDL_SCANCODE_F1] = SDLK_F1
SCANCODE2KEYCODE[SDL_SCANCODE_F2] = SDLK_F2
SCANCODE2KEYCODE[SDL_SCANCODE_F3] = SDLK_F3
SCANCODE2KEYCODE[SDL_SCANCODE_F4] = SDLK_F4
SCANCODE2KEYCODE[SDL_SCANCODE_F5] = SDLK_F5
SCANCODE2KEYCODE[SDL_SCANCODE_F6] = SDLK_F6
SCANCODE2KEYCODE[SDL_SCANCODE_F7] = SDLK_F7
SCANCODE2KEYCODE[SDL_SCANCODE_F8] = SDLK_F8
SCANCODE2KEYCODE[SDL_SCANCODE_F9] = SDLK_F9
SCANCODE2KEYCODE[SDL_SCANCODE_F10] = SDLK_F10
SCANCODE2KEYCODE[SDL_SCANCODE_F11] = SDLK_F11
SCANCODE2KEYCODE[SDL_SCANCODE_F12] = SDLK_F12
SCANCODE2KEYCODE[SDL_SCANCODE_F13] = SDLK_F13
SCANCODE2KEYCODE[SDL_SCANCODE_F14] = SDLK_F14
SCANCODE2KEYCODE[SDL_SCANCODE_F15] = SDLK_F15
SCANCODE2KEYCODE[SDL_SCANCODE_INSERT] = SDLK_INSERT
SCANCODE2KEYCODE[SDL_SCANCODE_DELETE] = SDLK_DELETE
SCANCODE2KEYCODE[SDL_SCANCODE_HOME] = SDLK_HOME
SCANCODE2KEYCODE[SDL_SCANCODE_END] = SDLK_END
SCANCODE2KEYCODE[SDL_SCANCODE_PAGEUP] = SDLK_PAGEUP
SCANCODE2KEYCODE[SDL_SCANCODE_PAGEDOWN] = SDLK_PAGEDOWN
SCANCODE2KEYCODE[SDL_SCANCODE_UP] = SDLK_UP
SCANCODE2KEYCODE[SDL_SCANCODE_DOWN] = SDLK_DOWN
SCANCODE2KEYCODE[SDL_SCANCODE_LEFT] = SDLK_LEFT
SCANCODE2KEYCODE[SDL_SCANCODE_RIGHT] = SDLK_RIGHT
SCANCODE2KEYCODE[SDL_SCANCODE_RETURN2] = SDLK_KP_ENTER
SCANCODE2KEYCODE[SDL_SCANCODE_RETURN] = SDLK_RETURN
SCANCODE2KEYCODE[SDL_SCANCODE_ESCAPE] = SDLK_ESCAPE
SCANCODE2KEYCODE[SDL_SCANCODE_PAUSE] = SDLK_PAUSE
SCANCODE2KEYCODE[SDL_SCANCODE_GRAVE] = SDLK_BACKQUOTE
SCANCODE2KEYCODE[SDL_SCANCODE_BACKSPACE] = SDLK_BACKSPACE
SCANCODE2KEYCODE[SDL_SCANCODE_TAB] = SDLK_TAB
SCANCODE2KEYCODE[SDL_SCANCODE_CAPSLOCK] = SDLK_CAPSLOCK
SCANCODE2KEYCODE[SDL_SCANCODE_SPACE] = SDLK_SPACE
SCANCODE2KEYCODE[SDL_SCANCODE_SLASH] = SDLK_SLASH
SCANCODE2KEYCODE[SDL_SCANCODE_BACKSLASH] = SDLK_BACKSLASH
SCANCODE2KEYCODE[SDL_SCANCODE_MINUS] = SDLK_MINUS
SCANCODE2KEYCODE[SDL_SCANCODE_UNKNOWN] = SDLK_PLUS
SCANCODE2KEYCODE[SDL_SCANCODE_EQUALS] = SDLK_EQUALS
SCANCODE2KEYCODE[SDL_SCANCODE_LEFTBRACKET] = SDLK_LEFTBRACKET
SCANCODE2KEYCODE[SDL_SCANCODE_RIGHTBRACKET] = SDLK_RIGHTBRACKET
SCANCODE2KEYCODE[SDL_SCANCODE_SEMICOLON] = SDLK_SEMICOLON
SCANCODE2KEYCODE[SDL_SCANCODE_APOSTROPHE] = SDLK_QUOTE
SCANCODE2KEYCODE[SDL_SCANCODE_COMMA] = SDLK_COMMA
SCANCODE2KEYCODE[SDL_SCANCODE_PERIOD] = SDLK_PERIOD
SCANCODE2KEYCODE[SDL_SCANCODE_LALT] = SDLK_LALT
SCANCODE2KEYCODE[SDL_SCANCODE_LCTRL] = SDLK_LCTRL
SCANCODE2KEYCODE[SDL_SCANCODE_LSHIFT] = SDLK_LSHIFT
SCANCODE2KEYCODE[SDL_SCANCODE_LALT] = SDLK_LALT
SCANCODE2KEYCODE[SDL_SCANCODE_LCTRL] = SDLK_LCTRL
SCANCODE2KEYCODE[SDL_SCANCODE_LSHIFT] = SDLK_LSHIFT
SCANCODE2KEYCODE[SDL_SCANCODE_PRINTSCREEN] = SDLK_PRINT
SCANCODE2KEYCODE[SDL_SCANCODE_SCROLLLOCK] = SDLK_SCROLLOCK
SCANCODE2KEYCODE[SDL_SCANCODE_LGUI] = SDLK_LMETA
SCANCODE2KEYCODE[SDL_SCANCODE_LGUI] = SDLK_LMETA
SCANCODE2KEYCODE[SDL_SCANCODE_LGUI] = SDLK_LSUPER
SCANCODE2KEYCODE[SDL_SCANCODE_RGUI] = SDLK_RSUPER
SCANCODE2KEYCODE[SDL_SCANCODE_UNKNOWN] = SDLK_UNKNOWN

KEYCODE2SCANCODE[SDLK_a] = SDL_SCANCODE_A
KEYCODE2SCANCODE[SDLK_b] = SDL_SCANCODE_B
KEYCODE2SCANCODE[SDLK_c] = SDL_SCANCODE_C
KEYCODE2SCANCODE[SDLK_d] = SDL_SCANCODE_D
KEYCODE2SCANCODE[SDLK_e] = SDL_SCANCODE_E
KEYCODE2SCANCODE[SDLK_f] = SDL_SCANCODE_F
KEYCODE2SCANCODE[SDLK_g] = SDL_SCANCODE_G
KEYCODE2SCANCODE[SDLK_h] = SDL_SCANCODE_H
KEYCODE2SCANCODE[SDLK_i] = SDL_SCANCODE_I
KEYCODE2SCANCODE[SDLK_j] = SDL_SCANCODE_J
KEYCODE2SCANCODE[SDLK_k] = SDL_SCANCODE_K
KEYCODE2SCANCODE[SDLK_l] = SDL_SCANCODE_L
KEYCODE2SCANCODE[SDLK_m] = SDL_SCANCODE_M
KEYCODE2SCANCODE[SDLK_n] = SDL_SCANCODE_N
KEYCODE2SCANCODE[SDLK_o] = SDL_SCANCODE_O
KEYCODE2SCANCODE[SDLK_p] = SDL_SCANCODE_P
KEYCODE2SCANCODE[SDLK_q] = SDL_SCANCODE_Q
KEYCODE2SCANCODE[SDLK_r] = SDL_SCANCODE_R
KEYCODE2SCANCODE[SDLK_s] = SDL_SCANCODE_S
KEYCODE2SCANCODE[SDLK_t] = SDL_SCANCODE_T
KEYCODE2SCANCODE[SDLK_u] = SDL_SCANCODE_U
KEYCODE2SCANCODE[SDLK_v] = SDL_SCANCODE_V
KEYCODE2SCANCODE[SDLK_w] = SDL_SCANCODE_W
KEYCODE2SCANCODE[SDLK_x] = SDL_SCANCODE_X
KEYCODE2SCANCODE[SDLK_y] = SDL_SCANCODE_Y
KEYCODE2SCANCODE[SDLK_z] = SDL_SCANCODE_Z
KEYCODE2SCANCODE[SDLK_0] = SDL_SCANCODE_0
KEYCODE2SCANCODE[SDLK_1] = SDL_SCANCODE_1
KEYCODE2SCANCODE[SDLK_2] = SDL_SCANCODE_2
KEYCODE2SCANCODE[SDLK_3] = SDL_SCANCODE_3
KEYCODE2SCANCODE[SDLK_4] = SDL_SCANCODE_4
KEYCODE2SCANCODE[SDLK_5] = SDL_SCANCODE_5
KEYCODE2SCANCODE[SDLK_6] = SDL_SCANCODE_6
KEYCODE2SCANCODE[SDLK_7] = SDL_SCANCODE_7
KEYCODE2SCANCODE[SDLK_8] = SDL_SCANCODE_8
KEYCODE2SCANCODE[SDLK_9] = SDL_SCANCODE_9
KEYCODE2SCANCODE[SDLK_F1] = SDL_SCANCODE_F1
KEYCODE2SCANCODE[SDLK_F2] = SDL_SCANCODE_F2
KEYCODE2SCANCODE[SDLK_F3] = SDL_SCANCODE_F3
KEYCODE2SCANCODE[SDLK_F4] = SDL_SCANCODE_F4
KEYCODE2SCANCODE[SDLK_F5] = SDL_SCANCODE_F5
KEYCODE2SCANCODE[SDLK_F6] = SDL_SCANCODE_F6
KEYCODE2SCANCODE[SDLK_F7] = SDL_SCANCODE_F7
KEYCODE2SCANCODE[SDLK_F8] = SDL_SCANCODE_F8
KEYCODE2SCANCODE[SDLK_F9] = SDL_SCANCODE_F9
KEYCODE2SCANCODE[SDLK_F10] = SDL_SCANCODE_F10
KEYCODE2SCANCODE[SDLK_F11] = SDL_SCANCODE_F11
KEYCODE2SCANCODE[SDLK_F12] = SDL_SCANCODE_F12
KEYCODE2SCANCODE[SDLK_F13] = SDL_SCANCODE_F13
KEYCODE2SCANCODE[SDLK_F14] = SDL_SCANCODE_F14
KEYCODE2SCANCODE[SDLK_F15] = SDL_SCANCODE_F15
KEYCODE2SCANCODE[SDLK_INSERT] = SDL_SCANCODE_INSERT
KEYCODE2SCANCODE[SDLK_DELETE] = SDL_SCANCODE_DELETE
KEYCODE2SCANCODE[SDLK_HOME] = SDL_SCANCODE_HOME
KEYCODE2SCANCODE[SDLK_END] = SDL_SCANCODE_END
KEYCODE2SCANCODE[SDLK_PAGEUP] = SDL_SCANCODE_PAGEUP
KEYCODE2SCANCODE[SDLK_PAGEDOWN] = SDL_SCANCODE_PAGEDOWN
KEYCODE2SCANCODE[SDLK_UP] = SDL_SCANCODE_UP
KEYCODE2SCANCODE[SDLK_DOWN] = SDL_SCANCODE_DOWN
KEYCODE2SCANCODE[SDLK_LEFT] = SDL_SCANCODE_LEFT
KEYCODE2SCANCODE[SDLK_RIGHT] = SDL_SCANCODE_RIGHT
KEYCODE2SCANCODE[SDLK_KP_ENTER] = SDL_SCANCODE_RETURN2
KEYCODE2SCANCODE[SDLK_RETURN] = SDL_SCANCODE_RETURN
KEYCODE2SCANCODE[SDLK_ESCAPE] = SDL_SCANCODE_ESCAPE
KEYCODE2SCANCODE[SDLK_PAUSE] = SDL_SCANCODE_PAUSE
KEYCODE2SCANCODE[SDLK_BACKQUOTE] = SDL_SCANCODE_GRAVE
KEYCODE2SCANCODE[SDLK_BACKSPACE] = SDL_SCANCODE_BACKSPACE
KEYCODE2SCANCODE[SDLK_TAB] = SDL_SCANCODE_TAB
KEYCODE2SCANCODE[SDLK_CAPSLOCK] = SDL_SCANCODE_CAPSLOCK
KEYCODE2SCANCODE[SDLK_SPACE] = SDL_SCANCODE_SPACE
KEYCODE2SCANCODE[SDLK_SLASH] = SDL_SCANCODE_SLASH
KEYCODE2SCANCODE[SDLK_BACKSLASH] = SDL_SCANCODE_BACKSLASH
KEYCODE2SCANCODE[SDLK_MINUS] = SDL_SCANCODE_MINUS
KEYCODE2SCANCODE[SDLK_PLUS] = SDL_SCANCODE_UNKNOWN
KEYCODE2SCANCODE[SDLK_EQUALS] = SDL_SCANCODE_EQUALS
KEYCODE2SCANCODE[SDLK_LEFTBRACKET] = SDL_SCANCODE_LEFTBRACKET
KEYCODE2SCANCODE[SDLK_RIGHTBRACKET] = SDL_SCANCODE_RIGHTBRACKET
KEYCODE2SCANCODE[SDLK_SEMICOLON] = SDL_SCANCODE_SEMICOLON
KEYCODE2SCANCODE[SDLK_QUOTE] = SDL_SCANCODE_APOSTROPHE
KEYCODE2SCANCODE[SDLK_COMMA] = SDL_SCANCODE_COMMA
KEYCODE2SCANCODE[SDLK_PERIOD] = SDL_SCANCODE_PERIOD
KEYCODE2SCANCODE[SDLK_LALT] = SDL_SCANCODE_LALT
KEYCODE2SCANCODE[SDLK_LCTRL] = SDL_SCANCODE_LCTRL
KEYCODE2SCANCODE[SDLK_LSHIFT] = SDL_SCANCODE_LSHIFT
KEYCODE2SCANCODE[SDLK_LALT] = SDL_SCANCODE_LALT
KEYCODE2SCANCODE[SDLK_LCTRL] = SDL_SCANCODE_LCTRL
KEYCODE2SCANCODE[SDLK_LSHIFT] = SDL_SCANCODE_LSHIFT
KEYCODE2SCANCODE[SDLK_PRINT] = SDL_SCANCODE_PRINTSCREEN
KEYCODE2SCANCODE[SDLK_SCROLLOCK] = SDL_SCANCODE_SCROLLLOCK
KEYCODE2SCANCODE[SDLK_LMETA] = SDL_SCANCODE_LGUI
KEYCODE2SCANCODE[SDLK_LMETA] = SDL_SCANCODE_LGUI
KEYCODE2SCANCODE[SDLK_LSUPER] = SDL_SCANCODE_LGUI
KEYCODE2SCANCODE[SDLK_RSUPER] = SDL_SCANCODE_RGUI
KEYCODE2SCANCODE[SDLK_UNKNOWN] = SDL_SCANCODE_UNKNOWN
