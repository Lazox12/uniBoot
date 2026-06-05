MAKE=make


all: ipxe_build

ipxe_build:
	# Enable NFS support
	sed -i 's/#undef\tDOWNLOAD_PROTO_NFS/#define\tDOWNLOAD_PROTO_NFS/' ipxe/src/config/general.h

	# Enable Ping support
	sed -i 's/\/\/#define\ PING_CMD/#define\ PING_CMD/' ipxe/src/config/general.h
	sed -i 's/\/\/#define\ IPSTAT_CMD/#define\ IPSTAT_CMD/' ipxe/src/config/general.h
	sed -i 's/\/\/#define\ REBOOT_CMD/#define\ REBOOT_CMD/' ipxe/src/config/general.h
	sed -i 's/\/\/#define\ POWEROFF/#define\ POWEROFF/' ipxe/src/config/general.h

	mkdir img -p

	cp bootstrap.ipxe ipxe/src/bootstrap.ipxe
	cp start.ipxe ipxe/src/start.ipxe


	$(MAKE) -C ipxe/src bin-x86_64-efi/snponly.efi EMBED=bootstrap.ipxe
	cp ipxe/src/bin-x86_64-efi/snponly.efi img
	
	$(MAKE) -C ipxe/src bin/undionly.kpxe bin-x86_64-efi/ipxe.efi bin-x86_64-efi/snponly.efi EMBED=start.ipxe

	cp ipxe/src/bin/undionly.kpxe img
	cp ipxe/src/bin-x86_64-efi/ipxe.efi img

clean:
	-rm -r img
	$(MAKE) -C ipxe/src clean
	-rm ipxe/src/bootstrap.ipxe
	-rm ipxe/src/start.ipxe