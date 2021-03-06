#!/usr/bin/env python3
'''
--> versione 3.4

passthroughfs.py - Example file system for pyfuse3
This file system mirrors the contents of a specified directory tree.
Caveats:
 * Inode generation numbers are not passed through but set to zero.
 * Block size (st_blksize) and number of allocated blocks (st_blocks) are not
   pa
'''

import os
import sys
import configparser
import re


# If we are running from the pyfuse3 source directory, try
# to load the module from there first.
basedir = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))
if (os.path.exists(os.path.join(basedir, 'setup.py')) and
        os.path.exists(os.path.join(basedir, 'src', 'pyfuse3.pyx'))):
    sys.path.insert(0, os.path.join(basedir, 'src'))

import pyfuse3
from argparse import ArgumentParser
import errno
import logging
import stat as stat_m
from pyfuse3 import FUSEError
from os import fsencode, fsdecode
from collections import defaultdict
import trio

import faulthandler

faulthandler.enable()

log = logging.getLogger(__name__)


class Operations(pyfuse3.Operations):
    enable_writeback_cache = True

    def __init__(self, source):
        super().__init__()
        self._inode_path_map = {pyfuse3.ROOT_INODE: source}
        self._lookup_cnt = defaultdict(lambda: 0)
        self._fd_inode_map = dict()
        self._inode_fd_map = dict()
        self._fd_open_count = dict()

    def _inode_to_path(self, inode):
        try:
            val = self._inode_path_map[inode]
        except KeyError:
            raise FUSEError(errno.ENOENT)

        if isinstance(val, set):
            # In case of hardlinks, pick any path
            val = next(iter(val))
        return val

    #################################################################################################################

    def _add_path(self, inode, path):
        log.debug('_add_path for %d, %s', inode, path)
        # print("path: ", path)

        # start = "/sys/class/gpio/"
        # print("start: ", start)
        # relative_path = os.path.relpath(path, start)
        # print("relative path ", relative_path)

        ultimopath.clear()
        ultimopath.insert(0, path)

        print("\n\nultimopath: ", ultimopath, "\n\n")

        print("\npath: ", path)



        print("la lista di gpio disponibili per test2 è: ", listgpio, "\n")

        if path == '/sys/class/gpio/export':
            print("1caso")
            export.clear()
            export.insert(0, 1)
            unexport.clear()
            unexport.insert(0, 0)
            if inode not in self._inode_path_map:
                self._inode_path_map[inode] = path
                return

            val = self._inode_path_map[inode]
            if isinstance(val, set):
                val.add(path)
            elif val != path:
                self._inode_path_map[inode] = {path, val}
            print("fine if\n\n")

        elif path == '/sys/class/gpio/unexport':
            print("2caso")
            export.clear()
            export.insert(0, 0)
            unexport.clear()
            unexport.insert(0, 1)
            if inode not in self._inode_path_map:
                self._inode_path_map[inode] = path
                return

            val = self._inode_path_map[inode]
            if isinstance(val, set):
                val.add(path)
            elif val != path:
                self._inode_path_map[inode] = {path, val}
            print("fine if\n\n")

        else:
            export.clear()
            export.insert(0, 0)
            unexport.clear()
            unexport.insert(0, 0)





        #x = re.search("gpio[10-28]", path)
        x = re.search("gpio\d{1,3}", path)
        print(x)  # this will print an object
        if x:
            print("\npath:", path)
            print("sì, c'è gpio*")
            print("il gpio presente nel path è:", x[0])
            gpio=x[0]

            if path.endswith('active_low'):
                print("caso active2")
                active.clear()
                active.insert(0, 1)
            else:
                active.clear()
                active.insert(0, 0)

            if path.endswith('direction'):
                print("caso direction2")
                direction.clear()
                direction.insert(0, 1)
            else:
                direction.clear()
                direction.insert(0, 0)

            if path.endswith('edge'):
                print("caso edge2")
                edge.clear()
                edge.insert(0, 1)
            else:
                edge.clear()
                edge.insert(0, 0)

            if path.endswith('value'):
                print("caso value2")
                value.clear()
                value.insert(0, 1)
            else:
                value.clear()
                value.insert(0, 0)



            #dobbiamo fare i controlli
            if gpio in listgpio:
                if inode not in self._inode_path_map:
                    self._inode_path_map[inode] = path
                    return

                val = self._inode_path_map[inode]
                if isinstance(val, set):
                    val.add(path)
                elif val != path:
                    self._inode_path_map[inode] = {path, val}
                print("fine if\n\n")
            else:
                print("gpio non in lista, non copio")




        else:
            print("\npath:", path)
            print("No match\n")
            #posso copiare tutto
            if inode not in self._inode_path_map:
                self._inode_path_map[inode] = path
                return

            val = self._inode_path_map[inode]
            if isinstance(val, set):
                val.add(path)
            elif val != path:
                self._inode_path_map[inode] = {path, val}


        '''               


        ultimopath.clear()
        ultimopath.insert(0, path)

        print("\n\nultimopath: ", ultimopath, "\n\n")

        print("\npath: ", path)
        pathclassgpio = re.compile(r'/sys/class/gpio/gpio*')

        if path == '/sys/devices/platform/soc/3f200000.gpio/gpio/gpiochip0' or path == '/sys/class/gpio' or path == '/sys/devices/platform/soc/3f200000.gpio/gpio' or path == '/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio' or path == '/sys/devices/platform/soc/3f200000.gpio/gpiochip0' or path == '/sys/class/gpio/gpiochip0' :
            
            print("fine if\n\n")






        

        elif path.startswith('sys/class/gpio/gpio*'):
            #ricavare gpio
            pathmodificata = os.path.relpath(path, '/sys/class/gpio/')
            basename = os.path.basename(path)
            basename = '/' + basename
            print("\n\n\npathmod:", pathmodificata, "basename:", basename, "\n\n\n")
            gpio = os.path.dirname(path)
            print("gpio:", gpio)

            #verificare se gpio appartiene alla lista di quelle visualizzabili per il container
            if gpio in listgpio:
                if inode not in self._inode_path_map:
                    self._inode_path_map[inode] = path
                    return

                val = self._inode_path_map[inode]
                if isinstance(val, set):
                    val.add(path)
                elif val != path:
                    self._inode_path_map[inode] = {path, val}
                print("fine if\n\n")
            else:
                print("gpio non in lista non copio")






        elif path.startswith('/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio/'):
            if path.endswith('active_low'):
                #ricavo gpio
                pathmodificata = os.path.relpath(path, '/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio/')
                basename = os.path.basename(path)
                basename = '/' + basename
                print("\n\n\npathmod:", pathmodificata, "basename:", basename, "\n\n\n")
                gpio = os.path.dirname(pathmodificata)
                print("gpio:", gpio)

                print("caso active2")
                active.clear()
                active.insert(0, 1)

                if gpio in listgpio:
                    if inode not in self._inode_path_map:
                        self._inode_path_map[inode] = path
                        return

                    val = self._inode_path_map[inode]
                    if isinstance(val, set):
                        val.add(path)
                    elif val != path:
                        self._inode_path_map[inode] = {path, val}
                    print("fine if\n\n")
                else:
                    print("non in lista non copio")

            elif path.endswith('direction'):
                pathmodificata = os.path.relpath(path, '/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio/')
                basename = os.path.basename(path)
                basename = '/' + basename
                print("\n\n\npathmod:", pathmodificata, "basename:", basename, "\n\n\n")
                gpio = os.path.dirname(pathmodificata)
                print("gpio:", gpio)

                print("caso direction2")
                direction.clear()
                direction.insert(0, 1)

                if gpio in listgpio:
                    if inode not in self._inode_path_map:
                        self._inode_path_map[inode] = path
                        return

                    val = self._inode_path_map[inode]
                    if isinstance(val, set):
                        val.add(path)
                    elif val != path:
                        self._inode_path_map[inode] = {path, val}
                    print("fine if\n\n")
                else:
                    print("non in lista non copio")

            elif path.endswith('edge'):
                pathmodificata = os.path.relpath(path, '/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio/')
                basename = os.path.basename(path)
                basename = '/' + basename
                print("\n\n\npathmod:", pathmodificata, "basename:", basename, "\n\n\n")
                gpio = os.path.dirname(pathmodificata)
                print("gpio:", gpio)

                print("caso edge2")
                edge.clear()
                edge.insert(0, 1)

                if gpio in listgpio:
                    if inode not in self._inode_path_map:
                        self._inode_path_map[inode] = path
                        return

                    val = self._inode_path_map[inode]
                    if isinstance(val, set):
                        val.add(path)
                    elif val != path:
                        self._inode_path_map[inode] = {path, val}
                    print("fine if\n\n")
                else:
                    print("non in lista non copio")

            elif path.endswith('uevent'):
                pathmodificata = os.path.relpath(path, '/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio/')
                basename = os.path.basename(path)
                basename = '/' + basename
                print("\n\n\npathmod:", pathmodificata, "basename:", basename, "\n\n\n")
                gpio = os.path.dirname(pathmodificata)
                print("gpio:", gpio)

                if gpio in listgpio:
                    if inode not in self._inode_path_map:
                        self._inode_path_map[inode] = path
                        return

                    val = self._inode_path_map[inode]
                    if isinstance(val, set):
                        val.add(path)
                    elif val != path:
                        self._inode_path_map[inode] = {path, val}
                    print("fine if\n\n")
                else:
                    print("non in lista non copio")

            elif path.endswith('value'):
                pathmodificata = os.path.relpath(path, '/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio/')
                basename = os.path.basename(path)
                basename = '/' + basename
                print("\n\n\npathmod:", pathmodificata, "basename:", basename, "\n\n\n")
                gpio = os.path.dirname(pathmodificata)
                print("gpio:", gpio)

                print("caso value2")
                value.clear()
                value.insert(0, 1)

                if gpio in listgpio:
                    if inode not in self._inode_path_map:
                        self._inode_path_map[inode] = path
                        return

                    val = self._inode_path_map[inode]
                    if isinstance(val, set):
                        val.add(path)
                    elif val != path:
                        self._inode_path_map[inode] = {path, val}
                    print("fine if\n\n")
                else:
                    print("non in lista non copio")



        else:
            print("caso non analizzato")
            print("3caso ripulisco export e unexport, value, active, edge")
            export.clear()
            export.insert(0, 0)
            unexport.clear()
            unexport.insert(0, 0)

            value.clear()
            value.insert(0, 0)

            active.clear()
            active.insert(0, 0)

            direction.clear()
            direction.insert(0, 0)

            edge.clear()
            edge.insert(0, 0)

            print("altro caso non copio nulla")



'''





    async def forget(self, inode_list):
        for (inode, nlookup) in inode_list:
            if self._lookup_cnt[inode] > nlookup:
                self._lookup_cnt[inode] -= nlookup
                continue
            log.debug('forgetting about inode %d', inode)
            assert inode not in self._inode_fd_map
            del self._lookup_cnt[inode]
            try:
                del self._inode_path_map[inode]
            except KeyError:  # may have been deleted
                pass

    async def lookup(self, inode_p, name, ctx=None):
        name = fsdecode(name)
        log.debug('lookup for %s in %d', name, inode_p)
        path = os.path.join(self._inode_to_path(inode_p), name)
        attr = self._getattr(path=path)
        if name != '.' and name != '..':
            self._add_path(attr.st_ino, path)
        return attr

    async def getattr(self, inode, ctx=None):
        if inode in self._inode_fd_map:
            return self._getattr(fd=self._inode_fd_map[inode])
        else:
            return self._getattr(path=self._inode_to_path(inode))

    def _getattr(self, path=None, fd=None):
        assert fd is None or path is None
        assert not (fd is None and path is None)
        try:
            if fd is None:
                stat = os.lstat(path)
            else:
                stat = os.fstat(fd)
        except OSError as exc:
            raise FUSEError(exc.errno)

        entry = pyfuse3.EntryAttributes()
        for attr in ('st_ino', 'st_mode', 'st_nlink', 'st_uid', 'st_gid',
                     'st_rdev', 'st_size', 'st_atime_ns', 'st_mtime_ns',
                     'st_ctime_ns'):
            setattr(entry, attr, getattr(stat, attr))
        entry.generation = 0
        entry.entry_timeout = 0
        entry.attr_timeout = 0
        entry.st_blksize = 512
        entry.st_blocks = ((entry.st_size + entry.st_blksize - 1) // entry.st_blksize)

        return entry

    async def readlink(self, inode, ctx):
        path = self._inode_to_path(inode)
        try:
            target = os.readlink(path)
        except OSError as exc:
            raise FUSEError(exc.errno)
        return fsencode(target)

    async def opendir(self, inode, ctx):
        return inode

    async def readdir(self, inode, off, token):
        path = self._inode_to_path(inode)
        log.debug('reading %s', path)
        entries = []
        for name in os.listdir(path):
            if name == '.' or name == '..':
                continue
            attr = self._getattr(path=os.path.join(path, name))
            entries.append((attr.st_ino, name, attr))

        log.debug('read %d entries, starting at %d', len(entries), off)

        # This is not fully posix compatible. If there are hardlinks
        # (two names with the same inode), we don't have a unique
        # offset to start in between them. Note that we cannot simply
        # count entries, because then we would skip over entries
        # (or return them more than once) if the number of directory
        # entries changes between two calls to readdir().
        for (ino, name, attr) in sorted(entries):
            if ino <= off:
                continue
            if not pyfuse3.readdir_reply(
                    token, fsencode(name), attr, ino):
                break
            self._add_path(attr.st_ino, os.path.join(path, name))

    async def unlink(self, inode_p, name, ctx):
        print("\nunlink\n\n")
        name = fsdecode(name)
        parent = self._inode_to_path(inode_p)
        path = os.path.join(parent, name)
        try:
            inode = os.lstat(path).st_ino
            os.unlink(path)
        except OSError as exc:
            raise FUSEError(exc.errno)
        if inode in self._lookup_cnt:
            self._forget_path(inode, path)

    async def rmdir(self, inode_p, name, ctx):
        print("\nrmdir\n\n")
        name = fsdecode(name)
        parent = self._inode_to_path(inode_p)
        path = os.path.join(parent, name)
        try:
            inode = os.lstat(path).st_ino
            os.rmdir(path)
        except OSError as exc:
            raise FUSEError(exc.errno)
        if inode in self._lookup_cnt:
            self._forget_path(inode, path)

    def _forget_path(self, inode, path):
        print("\nforgetpath\n\n")
        log.debug('forget %s for %d', path, inode)
        val = self._inode_path_map[inode]
        if isinstance(val, set):
            val.remove(path)
            if len(val) == 1:
                self._inode_path_map[inode] = next(iter(val))
        else:
            del self._inode_path_map[inode]

    async def symlink(self, inode_p, name, target, ctx):
        name = fsdecode(name)
        target = fsdecode(target)
        parent = self._inode_to_path(inode_p)
        path = os.path.join(parent, name)
        try:
            os.symlink(target, path)
            os.chown(path, ctx.uid, ctx.gid, follow_symlinks=False)
        except OSError as exc:
            raise FUSEError(exc.errno)
        stat = os.lstat(path)
        self._add_path(stat.st_ino, path)
        return await self.getattr(stat.st_ino)

    async def rename(self, inode_p_old, name_old, inode_p_new, name_new,
                     flags, ctx):
        if flags != 0:
            raise FUSEError(errno.EINVAL)

        name_old = fsdecode(name_old)
        name_new = fsdecode(name_new)
        parent_old = self._inode_to_path(inode_p_old)
        parent_new = self._inode_to_path(inode_p_new)
        path_old = os.path.join(parent_old, name_old)
        path_new = os.path.join(parent_new, name_new)
        try:
            os.rename(path_old, path_new)
            inode = os.lstat(path_new).st_ino
        except OSError as exc:
            raise FUSEError(exc.errno)
        if inode not in self._lookup_cnt:
            return

        val = self._inode_path_map[inode]
        if isinstance(val, set):
            assert len(val) > 1
            val.add(path_new)
            val.remove(path_old)
        else:
            assert val == path_old
            self._inode_path_map[inode] = path_new

    async def link(self, inode, new_inode_p, new_name, ctx):
        new_name = fsdecode(new_name)
        parent = self._inode_to_path(new_inode_p)
        path = os.path.join(parent, new_name)
        try:
            os.link(self._inode_to_path(inode), path, follow_symlinks=False)
        except OSError as exc:
            raise FUSEError(exc.errno)
        self._add_path(inode, path)
        return await self.getattr(inode)

    async def setattr(self, inode, attr, fields, fh, ctx):
        # We use the f* functions if possible so that we can handle
        # a setattr() call for an inode without associated directory
        # handle.
        if fh is None:
            path_or_fh = self._inode_to_path(inode)
            truncate = os.truncate
            chmod = os.chmod
            chown = os.chown
            stat = os.lstat
        else:
            path_or_fh = fh
            truncate = os.ftruncate
            chmod = os.fchmod
            chown = os.fchown
            stat = os.fstat

        try:
            if fields.update_size:
                truncate(path_or_fh, attr.st_size)

            if fields.update_mode:
                # Under Linux, chmod always resolves symlinks so we should
                # actually never get a setattr() request for a symbolic
                # link.
                assert not stat_m.S_ISLNK(attr.st_mode)
                chmod(path_or_fh, stat_m.S_IMODE(attr.st_mode))

            if fields.update_uid:
                chown(path_or_fh, attr.st_uid, -1, follow_symlinks=False)

            if fields.update_gid:
                chown(path_or_fh, -1, attr.st_gid, follow_symlinks=False)

            if fields.update_atime and fields.update_mtime:
                if fh is None:
                    os.utime(path_or_fh, None, follow_symlinks=False,
                             ns=(attr.st_atime_ns, attr.st_mtime_ns))
                else:
                    os.utime(path_or_fh, None,
                             ns=(attr.st_atime_ns, attr.st_mtime_ns))
            elif fields.update_atime or fields.update_mtime:
                # We can only set both values, so we first need to retrieve the
                # one that we shouldn't be changing.
                oldstat = stat(path_or_fh)
                if not fields.update_atime:
                    attr.st_atime_ns = oldstat.st_atime_ns
                else:
                    attr.st_mtime_ns = oldstat.st_mtime_ns
                if fh is None:
                    os.utime(path_or_fh, None, follow_symlinks=False,
                             ns=(attr.st_atime_ns, attr.st_mtime_ns))
                else:
                    os.utime(path_or_fh, None,
                             ns=(attr.st_atime_ns, attr.st_mtime_ns))

        except OSError as exc:
            raise FUSEError(exc.errno)

        return await self.getattr(inode)

    async def mknod(self, inode_p, name, mode, rdev, ctx):
        path = os.path.join(self._inode_to_path(inode_p), fsdecode(name))
        try:
            os.mknod(path, mode=(mode & ~ctx.umask), device=rdev)
            os.chown(path, ctx.uid, ctx.gid)
        except OSError as exc:
            raise FUSEError(exc.errno)
        attr = self._getattr(path=path)
        self._add_path(attr.st_ino, path)
        return attr

    ##########################################################################################################################################

    async def mkdir(self, inode_p, name, mode, ctx):
        path = os.path.join(self._inode_to_path(inode_p), fsdecode(name))
        print("path mkdir: ", path)

        start = "/sys/class/gpio/"
        print("start: ", start)
        relative_path = os.path.relpath(path, start)
        print("relative path ", relative_path)

        print("\n")
        print("listagpio2 utilizzabile per test2: ", listgpio)

        if path.startswith('/sys/class/gpio/'):
            start = '/sys/class/gpio/'
            relative_path = os.path.relpath(path, start)
            print("relative path ", relative_path)
            if relative_path in listgpio:
                print(relative_path, "trovato\n")
                try:
                    os.mkdir(path, mode=(mode & ~ctx.umask))
                    os.chown(path, ctx.uid, ctx.gid)
                except OSError as exc:
                    raise FUSEError(exc.errno)

            else:
                print("questo gpio non puoi usarlo2, puoi utilizzare dall'8 al 15!")

            attr = self._getattr(path=path)
            self._add_path(attr.st_ino, path)
            return attr

        elif path.startswith('/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio/'):
            start = '/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio/'
            relative_path = os.path.relpath(path, start)
            print("relative path ", relative_path)
            if relative_path in listgpio:
                print(relative_path, "trovato\n")
                try:
                    os.mkdir(path, mode=(mode & ~ctx.umask))
                    os.chown(path, ctx.uid, ctx.gid)
                except OSError as exc:
                    raise FUSEError(exc.errno)

            else:
                print("questo gpio non puoi usarlo2, puoi utilizzare dall'8 al 15!")

            attr = self._getattr(path=path)
            self._add_path(attr.st_ino, path)
            return attr

        else:
            print("caso non analizzato\n\n\n")

            try:
                os.mkdir(path, mode=(mode & ~ctx.umask))
                os.chown(path, ctx.uid, ctx.gid)
            except OSError as exc:
                raise FUSEError(exc.errno)

            attr = self._getattr(path=path)
            self._add_path(attr.st_ino, path)
            return attr

    async def statfs(self, ctx):
        root = self._inode_path_map[pyfuse3.ROOT_INODE]
        stat_ = pyfuse3.StatvfsData()
        try:
            statfs = os.statvfs(root)
        except OSError as exc:
            raise FUSEError(exc.errno)
        for attr in ('f_bsize', 'f_frsize', 'f_blocks', 'f_bfree', 'f_bavail',
                     'f_files', 'f_ffree', 'f_favail'):
            setattr(stat_, attr, getattr(statfs, attr))
        stat_.f_namemax = statfs.f_namemax - (len(root) + 1)
        return stat_

    async def open(self, inode, flags, ctx):
        if inode in self._inode_fd_map:
            fd = self._inode_fd_map[inode]
            self._fd_open_count[fd] += 1
            return pyfuse3.FileInfo(fh=fd)
        assert flags & os.O_CREAT == 0
        try:
            fd = os.open(self._inode_to_path(inode), flags)
        except OSError as exc:
            raise FUSEError(exc.errno)
        self._inode_fd_map[inode] = fd
        self._fd_inode_map[fd] = inode
        self._fd_open_count[fd] = 1
        return pyfuse3.FileInfo(fh=fd)

    async def create(self, inode_p, name, mode, flags, ctx):
        path = os.path.join(self._inode_to_path(inode_p), fsdecode(name))
        try:
            fd = os.open(path, flags | os.O_CREAT | os.O_TRUNC)
        except OSError as exc:
            raise FUSEError(exc.errno)
        attr = self._getattr(fd=fd)
        self._add_path(attr.st_ino, path)
        self._inode_fd_map[attr.st_ino] = fd
        self._fd_inode_map[fd] = attr.st_ino
        self._fd_open_count[fd] = 1
        return (pyfuse3.FileInfo(fh=fd), attr)

    async def read(self, fd, offset, length):
        os.lseek(fd, offset, os.SEEK_SET)
        return os.read(fd, length)

    async def write(self, fd, offset, buf):
        # ff=gpioint
        # f=gpio
        gpiobyte = buf.decode()
        print("buf: ", buf, "gpiobyte: ", gpiobyte)
        print("self: ", self, "offset: ", offset)

        print("export: ", export)
        print("unexport: ", unexport)
        print("direction: ", direction)
        print("value: ", value)
        print("activelow: ", active)
        print("edge: ", edge)

        if export[0] == 1 and unexport[0] == 0:
            print("1export")

            gpioint = int(gpiobyte)
            print("write\n buf: ", buf, "fd: ", fd)
            print("numerogpiobyte: ", gpiobyte)
            print("numerogpiointero: ", gpioint)

            gpio = str(gpioint)
            listgpio = listgpio2
            print("la lista di gpio disponibili per test2 è: ", listgpio, "\n")

            print(os.path.exists('/sys/class/gpio/gpio' + gpio + '/'))
            if gpioint in listgpio and not os.path.exists('/sys/class/gpio/gpio' + gpio + '/'):
                os.lseek(fd, offset, os.SEEK_SET)
                return os.write(fd, buf)
            else:
                print("errore")
                os.lseek(fd, offset, os.SEEK_SET)
                return 1
        elif export[0] == 0 and unexport[0] == 1:
            print("1unexport")

            gpioint = int(gpiobyte)
            print("write\n buf: ", buf, "fd: ", fd)
            print("numerogpiobyte: ", gpiobyte)
            print("numerogpiointero: ", gpioint)

            gpio = str(gpioint)
            listgpio = listgpio2
            print("la lista di gpio disponibili per test2 è: ", listgpio, "\n")

            print('/sys/class/gpio/gpio' + gpio + '/')
            print(os.path.exists('/sys/class/gpio/gpio' + gpio + '/'))
            if gpioint in listgpio and os.path.exists('/sys/class/gpio/gpio' + gpio + '/'):
                os.lseek(fd, offset, os.SEEK_SET)
                return os.write(fd, buf)
            else:
                print("errore")
                os.lseek(fd, offset, os.SEEK_SET)
                return 1
        # elif export[0] == 0 and unexport[0] == 0:
        #    print("1indefinito")
        else:

            print("1non dovrebbe capitare: echo direction value\n")
            print("buff:", buf)
            print("buf decodificato:", gpiobyte)
            gpiobyte = gpiobyte.strip('\n')
            print("buf decodificato senzsa\\n:", gpiobyte)

            if direction[0] == 1:
                print("caso direction:")
                if gpiobyte == 'in' or gpiobyte == 'out':
                    os.lseek(fd, offset, os.SEEK_SET)
                    return os.write(fd, buf)
                else:
                    print("errore")

                    pathmod = os.path.relpath(ultimopath[0], '/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio/')
                    basename = os.path.basename(ultimopath[0])
                    basename = '/' + basename
                    print("\n\n\npathmod:", pathmod, "basename:", basename, "\n\n\n")
                    gpio = os.path.dirname(pathmod)
                    print("gpio:", gpio)

                    valoredirezione = os.popen('cat /sys/class/gpio/' + gpio + '/direction').read()
                    valoredirezione = valoredirezione.strip('\n')

                    #print("valore direzione: ", valoredirezione)
                    #print('echo '+valoredirezione+' > /gpio_mnt/test2/sys/class/gpio/'+gpio+'/direction')
                    #cmd = 'echo '+valoredirezione+' > /gpio_mnt/test2/sys/class/gpio/'+gpio+'/direction'
                    #print(cmd)

                    #os.popen('./riavvio.sh test2').read()
                    os.system('./riavvio.sh test2')




                    #os.lseek(fd, offset, os.SEEK_SET)
                    return 1
            elif value[0] == 1:
                if gpiobyte == '1' or gpiobyte == '0':
                    gpioint = int(gpiobyte)
                    gpio = str(gpioint)
                    print("caso value:")

                    pathmod = os.path.relpath(ultimopath[0], '/sys/devices/platform/soc/3f200000.gpio/gpiochip0/gpio/')
                    basename = os.path.basename(ultimopath[0])
                    basename = '/'+basename
                    print("\n\n\npathmod:", pathmod, "basename:", basename, "\n\n\n")
                    gpio = os.path.dirname(pathmod)
                    print("gpio:",gpio)

                    valoredirezione = os.popen('cat /sys/class/gpio/'+gpio+'/direction').read()
                    valoredirezione = valoredirezione.strip('\n')
                    print("valore direzione: ", valoredirezione)


                    if valoredirezione == 'out':
                        if gpiobyte == '0' or gpiobyte == '1':
                            os.lseek(fd, offset, os.SEEK_SET)
                            return os.write(fd, buf)
                        else:
                            print("errore valori non accettati")
                            os.lseek(fd, offset, os.SEEK_SET)
                            os.system('./riavvio.sh test2')
                            return 1
                    else:
                        print("errore: non puoi modificare value se direction è in!")
                        os.lseek(fd, offset, os.SEEK_SET)
                        os.system('./riavvio.sh test2')
                        return 1
                else:
                    print("errore carattere")
                    os.system('./riavvio.sh test2')
                    return 1


            elif active[0] == 1:
                print("caso active:")
                if gpiobyte == '0' or gpiobyte == '1':
                    os.lseek(fd, offset, os.SEEK_SET)
                    return os.write(fd, buf)
                else:
                    print("errore")
                    os.lseek(fd, offset, os.SEEK_SET)
                    return 1

            else:
                print("errore2")
                os.lseek(fd, offset, os.SEEK_SET)
                return 1

            '''
            non funzionante perchè bisogna vedere quali parametri accetta, high e low non vanno bene

            elif edge[0] == 1:
                print("caso edge:")
                if gpiobyte == '0' or gpiobyte == '1':
                    os.lseek(fd, offset, os.SEEK_SET)
                    return os.write(fd, buf)
                else:
                    print("errore")
                    os.lseek(fd, offset, os.SEEK_SET)
                    return 1
            '''

    async def release(self, fd):
        if self._fd_open_count[fd] > 1:
            self._fd_open_count[fd] -= 1
            return

        del self._fd_open_count[fd]
        inode = self._fd_inode_map[fd]
        del self._inode_fd_map[inode]
        del self._fd_inode_map[fd]
        try:
            os.close(fd)
        except OSError as exc:
            raise FUSEError(exc.errno)


def init_logging(debug=False):
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(threadName)s: '
                                  '[%(name)s] %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    if debug:
        handler.setLevel(logging.DEBUG)
        root_logger.setLevel(logging.DEBUG)
    else:
        handler.setLevel(logging.INFO)
        root_logger.setLevel(logging.INFO)
    root_logger.addHandler(handler)


def parse_args(args):
    '''Parse command line'''

    parser = ArgumentParser()

    parser.add_argument('source', type=str,
                        help='Directory tree to mirror')
    parser.add_argument('mountpoint', type=str,
                        help='Where to mount the file system')
    parser.add_argument('--debug', action='store_true', default=False,
                        help='Enable debugging output')
    parser.add_argument('--debug-fuse', action='store_true', default=False,
                        help='Enable FUSE debugging output')

    return parser.parse_args(args)


def main():
    options = parse_args(sys.argv[1:])
    init_logging(options.debug)
    operations = Operations(options.source)

    log.debug('Mounting...')
    fuse_options = set(pyfuse3.default_options)
    fuse_options.add('fsname=passthroughfs')

    fuse_options.add('allow_other')

    if options.debug_fuse:
        fuse_options.add('debug')

    fuse_options.discard('default_permissions')
    pyfuse3.init(operations, options.mountpoint, fuse_options)

    try:
        log.debug('Entering main loop..')
        trio.run(pyfuse3.main)
    except:
        pyfuse3.close(unmount=False)
        raise

    log.debug('Unmounting..')
    pyfuse3.close()


if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.sections()
    config.read('example.ini')
    config.sections()

    # listgpio = ["gpiochip0", "gpiochip504", "export"]
    listgpio = ["gpiochip0", "gpiochip504", "export", "unexport"]

    for count in range(1, 27):
        # print(count, "gpio" + str(count))
        # print(config['gpiotest2']['gpio' + str(count)])
        if config['gpiotest2']['gpio' + str(count)] == 'yes':
            # print(count, "gpio" + str(count), "ok")
            listgpio.append("gpio" + str(count))
        print("\n")

    # listgpio = ["gpiochip0", "gpiochip504", "export", "unexport"]
    listgpio2 = []

    for count in range(1, 27):
        # print(count, "gpio" + str(count))
        # print(config['gpiotest2']['gpio' + str(count)])
        if config['gpiotest2']['gpio' + str(count)] == 'yes':
            # print(count, "gpio" + str(count), "ok")
            listgpio2.append(count)
        print("\n")

    export = [0]
    export.clear()
    unexport = [0]
    unexport.clear()
    direction = [0]
    direction.clear()
    value = [0]
    value.clear()
    active = [0]
    active.clear()
    edge = [0]
    edge.clear()

    ultimopath = ['']
    ultimopath.clear()

    main()
