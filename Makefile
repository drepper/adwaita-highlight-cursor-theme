rpm: srpm
	rpmbuild -rb SRPMS/adwaita-highlight-cursor-theme-*.rpm

srpm: clean
	make -C adwaita-cursors all
	make -C adwaita-cursors tarball
	rpmbuild -bs -D "_topdir $$PWD" adwaita-highlight-cursor-theme.spec

clean:
	$(MAKE) -C adwaita-cursors clean
	rm -fr adwaita-cursors/png
	rm -fr adwaita-cursors/png_hl
	rm -fr adwaita-cursors/Adwaita-highlight
	rm -fr BUILD BUILDROOT SRPMS RPMS
	rm -f adwaita-cursors.tar.gz

.PSEUDO: rpm srpm clean
.ONESHELL:
