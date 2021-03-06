/* ***** BEGIN LICENSE BLOCK *****
 * Version: MPL 1.1/GPL 2.0/LGPL 2.1
 *
 * The contents of this file are subject to the Mozilla Public License Version
 * 1.1 (the "License"); you may not use this file except in compliance with
 * the License. You may obtain a copy of the License at
 * http://www.mozilla.org/MPL/
 *
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
 * for the specific language governing rights and limitations under the
 * License.
 *
 * The Original Code is the Cisco Systems SIP Stack.
 *
 * The Initial Developer of the Original Code is
 * Cisco Systems (CSCO).
 * Portions created by the Initial Developer are Copyright (C) 2002
 * the Initial Developer. All Rights Reserved.
 *
 * Contributor(s):
 *  Enda Mannion <emannion@cisco.com>
 *  Suhas Nandakumar <snandaku@cisco.com>
 *  Ethan Hugg <ehugg@cisco.com>
 *
 * Alternatively, the contents of this file may be used under the terms of
 * either the GNU General Public License Version 2 or later (the "GPL"), or
 * the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
 * in which case the provisions of the GPL or the LGPL are applicable instead
 * of those above. If you wish to allow use of your version of this file only
 * under the terms of either the GPL or the LGPL, and not to allow others to
 * use your version of this file under the terms of the MPL, indicate your
 * decision by deleting the provisions above and replace them with the notice
 * and other provisions required by the GPL or the LGPL. If you do not delete
 * the provisions above, a recipient may use your version of this file under
 * the terms of any one of the MPL, the GPL or the LGPL.
 *
 * ***** END LICENSE BLOCK ***** */

#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <syslog.h>
#include <inttypes.h>

/**
 * platGenerateCryptoRand
 * @brief Generates a Random Number
 *
 * Generate crypto graphically random number for a desired length.
 * The function uses "secd" 's provided API. The random bytes are
 * generated by "secd" which runs as another process. The function
 * will be much slower than the cpr_rand(). This function should be
 * used when good random number is needed such as random number that
 * to be used for SRTP key for an example.
 *
 * @param[in] buf  - pointer to the buffer to store the result of random
 *                   bytes requested.
 * @param[in] len  - pointer to the length of the desired random bytes.
 *             When calling the function, the integer's value
 *             should be set to the desired number of random
 *             bytes ('buf' should be of at least this size).
 *             upon success, its value will be set to the
 *             actual number of random bytes being returned.
 *             (realistically, there is a maximum number of
 *             random bytes that can be returned at a time.
 *             if the caller request more than that, the
 *             'len' will indicate how many bytes are actually being
 *             returned) on failure, its value will be set to 0.
 *
 * @return 
 *     1 - success.
 *     0 - fail.
 *
 * @note This function MUST BE REWRITTEN BY THE VENDORS
 * @note The intent of this function is to generate a cryptographically strong
 * random number. Vendors can map this to HandyIron or OpenSSL random number
 * generation functions.
 */
int
platGenerateCryptoRand(uint8_t *buf, int *len)
{
    int fd;
    int rc = 0;
    ssize_t s;

    if ((fd = open("/dev/urandom", O_RDONLY)) == -1) {
        syslog(LOG_ERR, "Failed to open prng driver");
        return 0;
    }

    /*
     * Try to read the given amount of bytes from the PRNG device.  We do not
     * handle short reads but just return the number of bytes read from the
     * device.  The caller has to manage this.
     * E.g. gsmsdp_generate_key() in core/gsm/gsm_sdp_crypto.c
     */
    s = read(fd, buf, (size_t) *len);

    if (s > 0) {
        *len = s;
        rc = 1; /* Success */
    } else {
        *len = 0;
        rc = 0; /* Failure */
    }
        
    (void) close(fd);
    return rc;
}

