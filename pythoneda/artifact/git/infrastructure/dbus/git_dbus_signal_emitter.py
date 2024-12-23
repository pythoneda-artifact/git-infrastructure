# vim: set fileencoding=utf-8
"""
pythoneda/artifact/git/infrastructure/dbus/git_dbus_signal_emitter.py

This file defines the GitDbusSignalEmitter class.

Copyright (C) 2023-today rydnr's pythoneda-artifact/git-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared.infrastructure.dbus import DbusSignalEmitter
from typing import List


class GitDbusSignalEmitter(DbusSignalEmitter):
    """
    A Port that emits git-artifact events as d-bus signals.

    Class name: GitDbusSignalEmitter

    Responsibilities:
        - Connect to d-bus.
        - Emit git-artifact events as d-bus signals.

    Collaborators:
        - pythoneda.shared.application.PythonEDA: Requests emitting events.
        - pythoneda.shared.artifact.events.code.infrastructure.dbus events
    """

    def __init__(self):
        """
        Creates a new GitDbusSignalEmitter instance.
        """
        super().__init__()

    @classmethod
    def event_packages(cls) -> List[str]:
        """
        Retrieves the packages of the supported events.
        :return: The packages.
        :rtype: List[str]
        """
        return ["pythoneda.shared.artifact.events.code.infrastructure.dbus"]


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
